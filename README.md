# Gestion de Budget - PFA

This project is a desktop application for budget management, created as a part of a Final Year Project (PFA). The application allows users to manage their finances by categorizing budgets, managing transactions, tracking expenses, and setting financial goals.

## Features

- **User Authentication**: Secure login and registration system.
- **Dashboard**: Interactive dashboard providing an overview of the user's financial status.
- **Budget Categorization**: Add, modify, and delete budget categories and subcategories.
- **Transaction Management**: Add, modify, delete, search, and filter transactions.
- **Expense Tracking**: View the budgeted amount, amount spent, and remaining amount for each expense.
- **Budget Summary**: Display the total budget allocated, total amount spent, and remaining amount for each category.
- **Goals Management**: Define and track progress towards financial goals.
- **Notes Management**: Add, modify, delete, and access notes.

## Technologies Used

- **Python**: Programming language.
- **Tkinter**: GUI library for building the desktop application.
- **SQLite**: Database for storing user data and transactions.
- **Azure-ttk-theme**: For enhanced visual design of the application.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/soufianecherk/Gestion-de-budget-PFA.git
   ```
2. **Navigate to the project directory**
   ```bash
   cd Gestion-de-budget-PFA
   ```
3. **Install the required dependencies**
   Ensure you have Python installed. You can install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python main.py
   ```
2. **Login or Register**
   - If you are a new user, register an account.
   - If you already have an account, log in using your credentials.
3. **Explore the Dashboard**
   - Access different features like budget categorization, transaction management, and more through the interactive dashboard.

## File Structure

- `main.py`: Entry point of the application.
- `authentication.py`: Handles user authentication (login and registration).
- `dashboard.py`: Contains the main dashboard with access to various features.
- `transaction_screen.py`: Manages the transaction-related functionalities.
- `budget_screen.py`: Manages budget categorization.
- `goals_screen.py`: Manages financial goals.
- `notes_screen.py`: Manages notes.
- `database.py`: Handles database connections and queries.
- `utils.py`: Contains utility functions used across the application.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact soufiane.cherkaoui01@gmail.com
