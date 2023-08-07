# UnclePatStore
A web application for Uncle Pat's Online store (DARE) 

## Technical Components
* Backend - FAST API
* Frontend - Vue.js with Quasar Framework
* Databse - MYSQL (sqlite)

## Assumptions Made

List of assumptions made during the development of the project:

1. Uncle pat has yet to take images of his items (hence the lack of them in the website)
2. The website is a feel for Uncle Pat to see what an online store would look and feel like, hence there is no login or input-to-cart option yet.
3. Uncle Pat just wants to see what the user would see and how it can make changes to his store.

## Steps to Run the Application

Follow these steps to run the application locally:

```bash
# Clone the repository
git clone https://github.com/E-Laiii/UnclePatStore.git

# Create Virtual Environment
python -m venv unclepat_env
.\unclepat_env\Scripts\activate	

# Install dependencies
pip install -r requirements.txt
cd uncle_pat_store
npm install

# Run the backend API server
cd backend
uvicorn main:app --reload

# Run the frontend server
cd uncle_pat_store
npm run serve

```
Admin Credentials
* Username: adminpat
* Password: adminpat


## View Uncle Pat's online store

To view Uncle Pat's online store, follow the steps below:

1. Open your web browser (e.g., Chrome, Firefox, Safari).
2. Enter the following URL in the address bar: http://localhost:8080/ (replace 8080 with the port number the application is running on, if different).

The website will load, and you can now browse Uncle Pat's online store. Enjoy your shopping experience!

## Deploying on Cloud

To deploy the application on a cloud platform, follow these steps:

Step 1: Set up Cloud Environment: 
1. Set up an account on the cloud platform (e.g., AWS, GCP, Azure).
2. Install the necessary command-line tools and configure credentials.

Step 2: Set up Cloud Database server:
1. Create a cloud-based MySQL database using the cloud provider's database service (e.g., Amazon RDS, Google Cloud SQL, Azure Database for MySQL).
2. Note down the database connection details (host, port, username, password, database name).

Step 3: Dockerize the Application:
1. Create a Dockerfile for both the FastAPI backend and Vue.js frontend.
2. Build Docker images for both the backend and frontend of your application.
3. Push the Docker images to a container registry supported by your cloud provider (e.g., Docker Hub, Amazon ECR, Google Container Registry).

Step 4: Deploy Frontend & Backend: 
1. Create container instances where you will run your application.
2. Deploy the backend Docker image to a container instance with the appropriate environment variables (database connection details, etc.).
3. Deploy the frontend Docker image to a web server (e.g., Nginx, Apache) that serves your Vue.js application.

Step 5: Setup Networking & Security
1. Configure networking settings to allow external traffic to reach your application (e.g., open firewall ports, set up load balancers).
2. Enable HTTPS to secure your application's communication using SSL certificates.
3. Set up access control and security groups to restrict access to your application and database.

Step 6: Configure DNS and Domain Name
1. Register a domain name for your web application (e.g., example.com) from a domain registrar.
2. Configure DNS settings to point your domain name to the IP address of your cloud-based server.

## How to do this with a serverless component?
Containerize both FastAPI backend and Vue.js frontend and push the Docker image to a container registry (eg. Docker Hub). 
Deploy them on serverless functions using Google Cloud, Azure functions and AWS S3 for static hosting, Firebase Hosting

## Security Hardening Techniques on a Cloud Environment

When deploying the application on a cloud environment, these techniques can be considered:

1. Enable encryption at rest and in transit for sensitive data.
2. Implement network security groups to control inbound and outbound traffic. (only open selected ports for specific IPs)
3. Use security groups or access control lists to restrict access to specific IP addresses.
4. Regularly update and patch the operating system and software to address known vulnerabilities.
5. Set up strong authentication mechanisms, such as multi-factor authentication (MFA) and secure password policies.
6. Use secure protocols (e.g., HTTPS) to protect data transmission between clients and servers.
7. Monitor and log system activities to detect potential security incidents.
8. Implement access controls and role-based access control (RBAC) to limit user permissions.
9. Regularly back up data to protect against data loss and enable quick recovery in case of a security breach.
10. Regularly perform security audits and vulnerability assessments to identify and address security weaknesses.

##  Examples of Online Store

![Homepage Image](https://github.com/E-Laiii/UnclePatStore.git/images/UnclePatStore_Homepage.png)

![Adminpage Image](https://github.com/E-Laiii/UnclePatStore.git/images/UnclePatStore_Adminpage.png)

