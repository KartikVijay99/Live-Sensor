import sys  # To extract detailed error information

def error_message_detail(error, error_detail: sys):
    """
    Extracts error details including filename, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Extracts exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file where the error occurred
    line_number = exc_tb.tb_lineno  # Get the exact line number
    error_message = (
        f"Error occurred in file [{file_name}] at line [{line_number}]: {str(error)}"
    )
    return error_message

class SensorException(Exception):
    """
    Custom Exception Class for handling exceptions with detailed error messages.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
