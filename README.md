# Welcome to the Library Management System - Incyubyte Campus Placement Drive

## Objective
The goal of this project was to create a simple Library Management System for the Incyubyte company campus placement drive technical round. The system allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

## Features
- **Add Book**: Add new books to the library with detailed information.
- **Borrow Book**: Borrow available books from the library.
- **Return Book**: Return borrowed books to the library.
- **View Available Books**: View the list of books currently available in the library.

## Constraints
- **ISBN Number**: Every book must have a 13-digit ISBN number.

## Technology Stack
- **Language**: Python
- **Testing**: Pytest for Test-Driven Development (TDD)
- **prettytable** : for tabular output

## Project Structure
- `assests`: Containts the CSS for the test_report.html file 
- `src/`: Contains the main code for the Library Management System.
- `tests/`: Contains test cases for the system.
- `ouputdemo.txt`: A demo file showcasing the working of the Library Management System.
- `test_report.html`: An HTML file containing information about the test cases.
- `menu.py` : main app run script
- `requirement.txt`: All dependecies for the project
- `.gitignore` :  ignore the files and directories which are unnecessary to projec
- `venv` : virtual environment for the system 

## Development Practices
- **Clean Code**: Followed clean code principles to maintain readability and maintainability.
- **SOLID Principles**: Applied SOLID principles to ensure the system is scalable and easy to maintain.
- **Test-Driven Development (TDD)**: Developed the system using TDD to ensure high code quality and reliability.

## Tools Utilized
- **AI Tools**: Leveraged AI tools like Claude and ChatGPT to enhance project development, speed, and efficiency.

## How to Run
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/gojiyashailesh/library_management_system.git
    cd library-management-system
    ```
2. **Setup Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    python menu.py
    ```
4. **Run Tests**:
    ```bash
    pytest tests/ .
    ```
## Future Improvements

- Implement data persistence (database integration)
- Add user authentication and authorization
- Implement a graphical user interface
- Add more advanced search and filter options for books

## Conclusion
This project demonstrates the ability to design and implement a basic library management system while adhering to best practices in software development. The system is built with a focus on maintainability, scalability, and reliability, ensuring that it meets the requirements of the Incyubyte campus placement drive technical round.

## **Thank You**
Thank you for taking the time to review this project. I hope this system meets the expectations and requirements of the Incyubyte placement drive.
