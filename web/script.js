const dropArea = document.querySelector(".drag-area");
const dragText = dropArea.querySelector("header");
const browseButton = document.getElementById("browseButton");
const fileInput = document.getElementById("fileInput");

const checkButton = document.getElementById("checkButton");
const closeButton = document.getElementById("closeButton");
const resultModal = document.getElementById("resultModal");
const resultLabel = document.getElementById("resultLabel");
const resultConfidence = document.getElementById("resultConfidence");
const resultError = document.getElementById("resultError");

let selectedFile = null;

browseButton.addEventListener("click", () => {
  fileInput.click();
});

fileInput.addEventListener("change", function () {
  selectedFile = this.files[0];
  handleSelectedFile();
});

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();

  selectedFile = event.dataTransfer.files[0];
  handleSelectedFile();
});

checkButton.addEventListener("click", async () => {
  if (!selectedFile) {
    showResult({
      label: "No image selected",
      confidence: null,
      error: "Please upload an image before running the classifier.",
    });

    return;
  }

  await uploadImageForPrediction(selectedFile);
});

closeButton.addEventListener("click", () => {
  resultModal.classList.remove("open");
});

function handleSelectedFile() {
  if (!selectedFile) {
    return;
  }

  const validExtensions = ["image/jpeg", "image/jpg", "image/png"];

  if (!validExtensions.includes(selectedFile.type)) {
    alert("This is not a supported image file.");
    selectedFile = null;
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
    return;
  }

  dropArea.classList.add("active");
  showImagePreview(selectedFile);
}

function showImagePreview(file) {
  const fileReader = new FileReader();

  fileReader.onload = () => {
    const fileURL = fileReader.result;

    dropArea.innerHTML = `
      <img src="${fileURL}" alt="Uploaded preview" />
    `;
  };

  fileReader.readAsDataURL(file);
}

async function uploadImageForPrediction(file) {
  const formData = new FormData();
  formData.append("file", file);

  showResult({
    label: "Checking image...",
    confidence: null,
    error: "",
  });

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      showResult({
        label: "Prediction failed",
        confidence: null,
        error: data.error || "Unknown server error.",
      });

      return;
    }

    showResult({
      label: data.label,
      confidence: data.confidence,
      error: "",
    });
  } catch (error) {
    showResult({
      label: "Prediction failed",
      confidence: null,
      error: "Could not connect to the prediction server.",
    });
  }
}

function showResult({ label, confidence, error }) {
  resultLabel.textContent = label;
  resultError.textContent = error || "";

  if (confidence === null || confidence === undefined) {
    resultConfidence.textContent = "";
  } else {
    const confidencePercent = (confidence * 100).toFixed(2);
    resultConfidence.textContent = `Confidence: ${confidencePercent}%`;
  }

  resultModal.classList.add("open");
}