// Create context menu items on extension install
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "summarize",
    title: "Summarize this text",
    contexts: ["selection"],
  });

  chrome.contextMenus.create({
    id: "define",
    title: "Get meaning of this word",
    contexts: ["selection"],
  });
});

// Handle context menu clicks
chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  const selectedText = info.selectionText?.trim();
  if (!selectedText) return;

  if (info.menuItemId === "summarize") {
    const summary = await callSummarizationAPI(selectedText);
    showAlert(tab.id, "Summary:\n" + summary);
  } else if (info.menuItemId === "define") {
    if (selectedText.split(/\s+/).length > 1) {
      showAlert(tab.id, "Please select only one word to get meaning.");
      return;
    }
    const meaning = await getMeaning(selectedText);
    showAlert(tab.id, "Meaning:\n" + meaning);
  }
});

// Call Hugging Face summarization API
async function callSummarizationAPI(text) {
  try {
    const response = await fetch("https://api-inference.huggingface.co/models/facebook/bart-large-cnn", {
      method: "POST",
      headers: {
        Authorization: "Bearer YOUR_HF_TOKEN", // Replace with your key
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ inputs: text }),
    });

    if (!response.ok) {
      return "Sorry, couldn't summarize.";
    }

    const data = await response.json();
    return data[0]?.summary_text || "Sorry, couldn't summarize.";
  } catch (error) {
    console.error("Summarization API error:", error);
    return "Sorry, couldn't summarize.";
  }
}

// Call dictionary API for meaning
async function getMeaning(word) {
  try {
    const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
    if (!response.ok) {
      return "No meaning found.";
    }
    const data = await response.json();
    const definition = data[0]?.meanings?.[0]?.definitions?.[0]?.definition;
    return definition || "Meaning not available.";
  } catch (error) {
    console.error("Dictionary API error:", error);
    return "Error fetching meaning.";
  }
}

// Show alert popup in the current tab
function showAlert(tabId, message) {
  chrome.scripting.executeScript({
    target: { tabId },
    func: (msg) => alert(msg),
    args: [message],
  });
}

// Listen for messages from content script (on selection)
chrome.runtime.onMessage.addListener(async (request, sender) => {
  if (!sender.tab?.id) return;

  if (request.action === "summarize") {
    const summary = await callSummarizationAPI(request.text);
    chrome.tabs.sendMessage(sender.tab.id, { action: "showSummary", summary });
  } else if (request.action === "define") {
    const meaning = await getMeaning(request.text);
    chrome.tabs.sendMessage(sender.tab.id, { action: "showMeaning", meaning });
  } else if (request.action === "clear") {
    // Optionally handle clear action if needed
    chrome.tabs.sendMessage(sender.tab.id, { action: "clear" });
  }
});
