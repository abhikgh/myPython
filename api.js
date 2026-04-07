import { GoogleGenerativeAI } from "@google/generative-ai";

import dotenv from "dotenv";
dotenv.config()

const googleGenAI = new GoogleGenerativeAI(process.env.apiKey);

async function main() {
  try {

    console.log("Generating content...");

    const prompt = "Write a short story about a cat who learns to play the piano.";
    const model = googleGenAI.getGenerativeModel({ model: "gemini-2.5-flash" });

    const result = await model.generateContent(prompt);
    const response = await result.response;

    const text = response.text();
    console.log(text);

  } catch (error) {
    console.error("Error generating content:", error);
    throw error;
  }
}

main();