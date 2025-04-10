# CP3407 Orientation AI Assistant Project 🤖
This project is created by Group-8.<br>
Team members: Bao Linh Van, Yunqiu Zhu, Vincent Thendean, and Cao Shaung Li <br>
**Weekly workshops**: https://docs.google.com/document/d/1hSm7TEy8SbGbZT-J8jzUGchv5jHCJfkhwtOCgqO67co/edit?usp=sharing <br>
**Figma link to Prototype**:  <br>
**Figma link to Big Board**:  <br>

## Project Overview
The purpose of this project is to develop a **web-based chatbot application** tailored to enhance the experience and engagement of new students during their **orientation program**. This chatbot will serve as an interactive digital assistant, providing immediate and accurate responses to questions about the orientation program and fostering connections among new students through suggested games and interactions. The project development duration is **10 weeks**. The budget is S$0, as it is a school initiative. All resources, materials, and tools will be obtained from free or existing school supplies and online resources. This approach fosters creativity and resourcefulness, ensuring the project remains viable within a zero-budget framework.
## Objective
The objective of the project includes:
- Develop a web-based chatbot capable of answering questions about the orientation program, based on information shared by the Student Affairs department.
- Promote engagement and interaction among new students by suggesting games and collaborative activities.
- Create a scalable and user-friendly platform that integrates seamlessly with the existing orientation process.
## Features
The features of Orientation AI Assitiant Project consist of:
- Information Support: Provide prompt responses to frequently asked questions about the orientation schedule, locations, events, and key policies or procedures
- Interative Suggestions: Recommend games, interactive activities, team-building exercises, and group discussions to encourage socialization among students
- Feedback Collection: Collect feedback on the chatbot’s performance to enhance future iterations and use it to improve the orientation program
## Technology Stack
### Frontend
- **Streamlit**: A Python library for creating interactive web applications with minimal effort.
- **Flask**: A lightweight WSGI web application framework for serving APIs and handling backend logic.

### Backend
- **Programming Language**: 
  - **Python**: A versatile choice for backend development, utilized throughout the stack.
- **Streamlit**: Serves as both the frontend and backend, simplifying application architecture and enabling quick deployment.

### AI/NLP
- **Chatbot Service**:
  - **Claude API**: For natural language processing and generating responses.
  - **Gemini API**: For AI embeddings, enhancing contextual understanding.

- **Translation**:
  - **Google Translate Library**: Imported into Python to translate responses to different languages using the `googletrans` method.
  
- **Vectorstore**:
  - **FAISS**: For efficient similarity search and clustering of embeddings.
  - **LangChain**: Facilitates the integration of LLMs (like Gemini) with various data sources and manages conversational flows effectively.

- **Prompt Engineering**:
  - **Model Training**: Develop effective prompts to enhance the model's understanding and response capabilities.
  - **Query Optimization**: Dynamically adjust prompts based on conversation context to improve relevance and accuracy.

### Database
- **MongoDB**: A NoSQL database used to store orientation information and user feedback.

### Version Control
- **Git**: For version control, enabling tracking of changes and collaboration.
- **GitHub**: For repository hosting and collaboration, facilitating team workflows and open-source contributions.
  
## Data and Privacy
The chatbot will be trained on data provided by the Student Affairs department, including orientation schedules, event descriptions, and FAQs. 
All data will be handled with strict adherence to privacy regulations, ensuring that student information and interactions remain confidential.

# Desgin
## Chatbot UI Component
![Chatbot UI](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Chatbot%20UI.jpg)

The Chatbot UI component is designed to enhance user interaction through a clean and intuitive interface, specifically tailored for new students arriving at JCU Singapore. It serves as a virtual assistant, providing essential information and support related to the JCU Orientation, helping students navigate their new environment with ease.

### Key Features

#### Logo Display
- Prominently features the JCU logo, establishing brand identity and trust.

#### Multi-Language Support
- Offers users the ability to choose their preferred language (Chinese or English), enhancing accessibility for a diverse audience.

#### Chat Area
- The main section where users can interact with the chatbot. It provides responsive answers to orientation-related queries and general information.

#### Quick Questions Feature
- To facilitate fast responses, a "Quick Questions" option allows students to click on common inquiries, ensuring they receive immediate assistance for frequently asked questions.

#### Chat History
- Users can view previous interactions, allowing for easy reference to past questions and responses, thus improving user experience.

#### User Feedback and Settings
- Includes options for feedback and settings adjustments, enabling users to customize their experience and communicate their thoughts on the chatbot's performance.

#### Help Section
- Provides additional assistance and resources for users, ensuring they have access to all necessary information.

### Overall UI Design
The design is minimalistic yet functional, featuring a user-friendly layout that guides users seamlessly through their inquiries. The use of clear typography and structured elements ensures that information is easily digestible, making it suitable for users seeking quick and efficient responses.

## UML Class Diagram 
![UML Class Diagram](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/UML_Class_Diagram.jpg)
This diagram provides a clear overview of the chatbot system’s architecture. It visually maps out how different components—such as the **frontend (Streamlit), backend (Flask), FAQ generation module, embedding process, and MongoDB** database—work together. The diagram helps illustrate the main data flow: a user sends a question through the frontend, the backend receives it and forwards it to the FAQ module, which either retrieves an answer from the database or uses vector search and a language model to generate a response. It also shows how files are uploaded and processed into embeddings, which are stored for future reference. The overall workflow depicted in the diagram starts from user interaction, flows through the backend to data processing and storage, and returns a response—demonstrating how information is passed through the system in a modular and structured way.
## UML Sequence Diagram 
![UML Sequence Diagram](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/UML_Sequence_Diagram.jpg)
This sequence diagram visualizes the full workflow of a user submitting a question and receiving an AI-generated answer. It begins with the user entering a question through the Streamlit frontend, where the system detects and translates the language if needed. The question is then sent to the Flask backend via a POST request. The backend passes the query to the FAQ processor, which first checks MongoDB for any existing answers. If no answer is found, it retrieves similar documents using FAISS and generates a new response using a language model like Claude or Gemini. The final answer is then stored in the database and returned to the frontend, where it is translated back to the user’s language if necessary and displayed. This diagram clearly illustrates the step-by-step interaction between system components involved in delivering a complete user experience.
## Database Design
![Database Design](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Database_Diagram.jpg)
This ER diagram presents a simplified view of the database structure used in the chatbot system. It highlights the relationships between uploaded files, FAQs, vector embeddings, user feedback, and stored content in MongoDB GridFS. Each uploaded file is associated with metadata such as filename, file type, and upload time, and is linked to both the GridFS storage system and potential FAQ entries generated from its content. Files are also connected to vector indexes stored in the VectorStore collection, enabling efficient semantic search. Additionally, the diagram shows how users submit feedback, which is stored with timestamps. Overall, this diagram helps illustrate how the data is organized and how documents, embeddings, and user interactions are connected in the backend.
# Implementation/Code
## Iteration 1
![Iteration 1](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Iteration%201.jpg)
![Iteration 1: team velocity, feedback, calculated velocity for Iteration 2](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Iteration%201%20Description.jpg)
## Iteration 2
![Iteration 2](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Iteration%202.jpg)
![Iteration 2: team velocity, feedback, calculated velocity for Iteration 3](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Iteration%202%20Description.jpg)
## Iteration 3
![Iteration 3](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Iteration%203.jpg)
# Testing

