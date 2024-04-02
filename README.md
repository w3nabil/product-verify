# Product Verification WEBAPP

## Requirements 

- Python 3.12 or higher
- Flask
- Flask SQLAlchemy

## Modification Need in file 
--> pyvenv.cfg 
--> replace .env.example with .env and add the necessary things 

## PROS 
- Faster and Easy to manage
- Doesn't require extra DB server 
- BEST for low-scale business

## CONS 
- DB can be injectable , Not good for keeping secret data such as password email and many more
- May not work fine if the server usage is high

## Screenshot from WEBAPP 
Path : /
![image](https://github.com/w3nabil/product-verify/assets/124899245/52815d97-c574-4428-b183-ff7dd4e35a30)
Path : /verify (if the product id and key found in the database)
![image](https://github.com/w3nabil/product-verify/assets/124899245/b11774e7-56de-4acd-8d53-48a45c47e3f4)
Path : /verify (if the product id or key doesn't match or not found in database)
![image](https://github.com/w3nabil/product-verify/assets/124899245/fc4a7bd1-5dc6-47ba-a1bc-ffa85ee3018d)
Path : /add 
![image](https://github.com/w3nabil/product-verify/assets/124899245/da2f95c5-e640-41d3-900d-2cd8b6394579)

## Things which makes no sense 
- Admin panel isn't added because of the possible injection, there is always a chance hackers can steal data
- path : /add is open for everyone.
- Several input checking wasn't done.
- Advanced CSS and JS module wasn't added.

## NOTE 
- This project is just a test project made by me. Several things will be added later. The version of the app you see is still in beta phrase you may see a lot bugs and more. Thank you for understanding.

