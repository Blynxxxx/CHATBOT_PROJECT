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
## App Basic Architecture

## UML Class Diagram 
![UML Class Diagram](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/UML_Class_Diagram.jpg)
## UML Sequence Diagram 
![UML Sequence Diagram](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/UML_Sequence_Diagram.jpg)
## Database Design
![Database Design](https://github.com/Blynxxxx/CHATBOT_PROJECT/blob/main/images/Database_Diagram.jpg)
# Implementation/Code

# Testing

