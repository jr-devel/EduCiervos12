instructions = [
    """
    CREATE TABLE IF NOT EXISTS user (
        user_id INT PRIMARY KEY AUTO_INCREMENTABLE NOT NULL,
        user_name TEXT NOT NULL,
        user_boleta INT NOT NULL,
        user_mail TEXT NOT NULL,
        user_results TEXT NOT NULL
    )
    """
]