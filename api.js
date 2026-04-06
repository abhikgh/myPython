//npm install @google/generative-ai

import {GoogleGenerativeAI} from "@google/generative-ai";

const apiKey = "AIzaSyAuQkN_NYe3sjz8CVTkbUUMm5eyDVL-hlA";

const googleGenAI = new GoogleGenerativeAI(apiKey);

async function main() {
  try {

    console.log("Generating content...");
    
    const prompt = "Write a short story about a robot learning to love.";
    const model = googleGenAI.getGenerativeModel({ model: "gemini-1.5-pro" });

    const response = await googleGenAI.generateContent({
      model,
      prompt,
    });
    const text =  response.text;
    console.log(text);
  } catch (error) {
    console.error("Error generating content:", error);
    throw error;
  }
}