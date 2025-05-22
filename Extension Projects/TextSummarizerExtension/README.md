
# Text Summarizer Chrome Extension

This Chrome extension allows users to quickly summarize selected text or get the meaning of a single word directly from any webpage.  
It provides context menu options on text selection, and a popup UI for manual input and summarization.

---

## Features

- **Summarize selected text** via right-click context menu or popup input.
- **Get the meaning of a selected word** via context menu.
- **Popup UI** with input textarea and summarize button.
- Copy summarized or defined text to clipboard from the popup.
- Lightweight, simple design with clean UI.

---

## How to Use

### From webpage

1. Select text on any webpage.
2. Right-click the selection.
3. Choose **"Summarize this text"** to get a summary of the selected text.
4. Or choose **"Get meaning of this word"** (only single words) to get its definition.

A popup will appear at the bottom-right of the page showing the summary or meaning, with a copy button.

### From the popup UI

1. Click the extension icon to open the popup.
2. Paste or type text into the textarea.
3. Click **Summarize** to get a summary displayed within the popup.

---

## Installation

1. Clone or download this repository.
2. Open Chrome and go to `chrome://extensions/`.
3. Enable **Developer mode** (toggle top-right).
4. Click **Load unpacked** and select the extension folder.
5. The extension will be added to Chrome and ready to use.

---

## Files

- `content.js` - Handles text selection and showing the popup summary/meaning on the page.
- `background.js` - Manages context menu, calls external APIs for summarization and dictionary definitions.
- `popup.html` - Popup UI for manual text input and summarization.
- `manifest.json` - Extension manifest configuration.

---

## APIs Used

- **Hugging Face Summarization API**  
  Model: `facebook/bart-large-cnn`  
  (Replace API key in `background.js` with your own)

- **Dictionary API**  
  Free dictionary API from `https://api.dictionaryapi.dev`

---

## Notes

- Summarization requires an API key from Hugging Face; make sure to replace the placeholder key in `background.js` with your own.
- Meaning lookup works only for single words.
- The popup and page popup can both be used independently.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Feel free to submit issues or pull requests to improve the extension!

---

## Contact

Created by [Your Name].  
Feel free to reach out for questions or suggestions.
