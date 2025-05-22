let timeoutId;
let previousText = "";

// Create or get the popup div to show summary/meaning + copy button
function getOrCreatePopup() {
  let popup = document.getElementById("extension-popup");
  if (!popup) {
    popup = document.createElement("div");
    popup.id = "extension-popup";
    Object.assign(popup.style, {
      position: "fixed",
      bottom: "20px",
      right: "20px",
      maxWidth: "320px",
      padding: "15px",
      backgroundColor: "rgba(0, 0, 0, 0.8)",
      color: "white",
      borderRadius: "8px",
      boxShadow: "0 0 10px rgba(0,0,0,0.5)",
      zIndex: 999999,
      fontSize: "14px",
      lineHeight: "1.4",
      whiteSpace: "pre-wrap",
      display: "none",
      userSelect: "text",
      position: "fixed",
    });

    // Close button
    const closeBtn = document.createElement("button");
    closeBtn.textContent = "✕";
    Object.assign(closeBtn.style, {
      position: "absolute",
      top: "5px",
      right: "8px",
      background: "transparent",
      border: "none",
      color: "white",
      fontSize: "16px",
      cursor: "pointer",
    });
    closeBtn.onclick = () => {
      popup.style.display = "none";
      document.getElementById("popup-content").textContent = "";
      document.getElementById("copy-btn").style.display = "none";
      previousText = "";
      chrome.runtime.sendMessage({ action: "clear" });
    };
    popup.appendChild(closeBtn);

    // Content container
    const contentDiv = document.createElement("div");
    contentDiv.id = "popup-content";
    contentDiv.style.marginBottom = "10px";
    popup.appendChild(contentDiv);

    // Copy button
    const copyBtn = document.createElement("button");
    copyBtn.id = "copy-btn";
    copyBtn.textContent = "Copy";
    Object.assign(copyBtn.style, {
      padding: "6px 12px",
      backgroundColor: "#007bff",
      border: "none",
      color: "white",
      borderRadius: "4px",
      cursor: "pointer",
      display: "none",
    });
    copyBtn.onclick = () => {
      const text = contentDiv.textContent;
      navigator.clipboard.writeText(text).then(() => {
        copyBtn.textContent = "Copied!";
        setTimeout(() => (copyBtn.textContent = "Copy"), 2000);
      });
    };
    popup.appendChild(copyBtn);

    document.body.appendChild(popup);
  }
  return popup;
}

document.addEventListener("selectionchange", () => {
  clearTimeout(timeoutId);

  timeoutId = setTimeout(() => {
    const selectedText = window.getSelection().toString().trim();

    // If no text selected but previously something was, clear popup
    if (!selectedText && previousText) {
      chrome.runtime.sendMessage({ action: "clear" });
      previousText = "";
      return;
    }

    if (selectedText === previousText) return;

    previousText = selectedText;

    if (selectedText.length > 10) {
      chrome.runtime.sendMessage({ action: "summarize", text: selectedText });
    } else if (selectedText.length > 0 && selectedText.split(/\s+/).length === 1) {
      chrome.runtime.sendMessage({ action: "define", text: selectedText });
    }
  }, 500);
});

chrome.runtime.onMessage.addListener((message) => {
  const popup = getOrCreatePopup();
  const contentDiv = document.getElementById("popup-content");
  const copyBtn = document.getElementById("copy-btn");

  if (message.action === "showSummary") {
    contentDiv.textContent = "Summary:\n" + message.summary;
    popup.style.display = "block";
    copyBtn.style.display = "inline-block";
    copyBtn.textContent = "Copy";
  } else if (message.action === "showMeaning") {
    contentDiv.textContent = "Meaning:\n" + message.meaning;
    popup.style.display = "block";
    copyBtn.style.display = "inline-block";
    copyBtn.textContent = "Copy";
  } else if (message.action === "clear") {
    popup.style.display = "none";
    contentDiv.textContent = "";
    copyBtn.style.display = "none";
    previousText = "";
  }
});
