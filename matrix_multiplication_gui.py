import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox


class MatrixMultiplicationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix Multiplication")

        # Create UI elements
        self.matrix1_label = QLabel("Enter the first matrix (rows separated by newlines, values by spaces):")
        self.matrix1_input = QTextEdit()
        
        self.matrix2_label = QLabel("Enter the second matrix (rows separated by newlines, values by spaces):")
        self.matrix2_input = QTextEdit()

        self.multiply_button = QPushButton("Multiply Matrices")
        self.multiply_button.clicked.connect(self.perform_multiplication)

        self.result_label = QLabel("Result:")
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix1_input)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.matrix2_input)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def perform_multiplication(self):
        try:
            # Get input from text fields
            matrix1_text = self.matrix1_input.toPlainText()
            matrix2_text = self.matrix2_input.toPlainText()

            # Convert text inputs to NumPy arrays
            A = self.text_to_array(matrix1_text)
            B = self.text_to_array(matrix2_text)

            # Perform matrix multiplication
            result = A @ B

            # Display the result in the result text box
            result_str = "\n".join(" ".join(map(str, row)) for row in result)
            self.result_display.setPlainText(result_str)

        except ValueError as ve:
            QMessageBox.critical(self, "Error", f"Invalid input: {str(ve)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def text_to_array(self, text):
        """Converts multi-line string input into a NumPy array."""
        rows = text.strip().split("\n")
        return np.array([list(map(int, row.split())) for row in rows])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixMultiplicationApp()
    window.show()
    sys.exit(app.exec_())