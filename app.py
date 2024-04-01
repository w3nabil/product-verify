"""
This module contains the flask running function.

Author: NABIL
Date: 29/03/2024
"""
from pack import server

if __name__ == '__main__':   
    app = server()
    app.run(host='0.0.0.0', port=5000, debug=True)
