# Certificate Validation using Blockchain

---

You can read my article on [Medium](https://medium.com/@sahilkadam257/certificate-validation-using-blockchain-3c560fd1738c) to get a better overall understanding of this project.

---

## Introduction

This project provides a Blockchain based solution for generating and verifying digital certificates. The certificate information (uid, candidate_name, course_name, org_name, ipfs_hash) is stored on the blockchain. First, the certificate pdf is generated and stored onto IPFS using Pinata service. Then, the IPFS hash obtained is stored on the blockchain along with other information.

The system comprises of 2 main entities:
- **Institute**: Responsible for generating and issuing certificates. Has the functionality to generate and view certificates.

- **Verifier**: Responsible for verifying certificates. Has the functionality to verify certificates by either uploading a certificate pdf or by inputting the certificate id.

---

## Features

- **Smart Contract:** Utilizes a Solidity smart contract to manage and store certificate details on the Ethereum blockchain.
- **IPFS Integration:** Stores certificate PDFs on IPFS via Pinata for decentralized and secure file storage.
- **Firebase Authentication:** Uses Firebase for authentication.
- **Streamlit App:** Provides a user-friendly interface for generating and verifying certificates.

---

## Getting Started

Clone the repository using the command:
```sh
git clone https://github.com/Sahil181045/Certificate-Validation-System.git
```
You can run the project either through:
- [Local Setup](#local-setup)
- [Using Docker](#using-docker) (Recommended)

---

## Local Setup

### Prerequisites

- **Node version >= 21.0.0**  
Truffle requires node version 16 or higher. The node version on my machine on which I tested this project was 21.0.0. You can try a lower node version (>=16.0).

- **Python version >= 3.9.10**  
    Python version 3.9.10 or higher is recommended but other versions may also work.

- **Globally installed packages for Truffle and Ganache-cli**  

    ```sh
    npm install -g truffle
    ```
    ```sh
    npm install -g ganache-cli
    ```

- **Python packages**  
    In the project's root directory, exececute the command:
    ```sh
    pip install -r application/requirements.txt
    ```
    It is recommended to create a virtual environment and then install the requirements and run the streamlit application in that virtual environment.

- **Firebase project setup**  
    Create a project on [Firebase Console](https://console.firebase.google.com/). This will be used to setup an authentication service in the project. Enable email/password sign in method under Authentication in the Build section.
    Go to project settings. Add new app. Note the following details in a .env file inside the project's root directory.
    ```sh
    FIREBASE_API_KEY
    FIREBASE_AUTH_DOMAIN
    FIREBASE_DATABASE_URL (Set this to "")
    FIREBASE_PROJECT_ID
    FIREBASE_STORAGE_BUCKET
    FIREBASE_MESSAGING_SENDER_ID
    FIREBASE_APP_ID
    ```

- **Pinata account setup**  
    Create an account on [Pinata](https://app.pinata.cloud/). Go to the API keys section and generate a new key. Note the API key and secret key in .env file.

- **.env file**  
    Finally your .env file should contain the following things:

    ```sh
    PINATA_API_KEY = "<Your Pinata API key>"
    PINATA_API_SECRET = "<Your Pinata Secret Key>"
    FIREBASE_API_KEY = "<Your Firebase API key>"
    FIREBASE_AUTH_DOMAIN = "<Your Firebase auth domain>"
    FIREBASE_DATABASE_URL = ""
    FIREBASE_PROJECT_ID = "<Your Firebase project id>"
    FIREBASE_STORAGE_BUCKET = "<Your Firebase Storage Bucket>"
    FIREBASE_MESSAGING_SENDER_ID = "<Your Firebase messaging sender id>"
    FIREBASE_APP_ID = "<Your Firebase app id>"
    institute_email = "institute@gmail.com" # Feel free to modify this
    institute_password = "123456" # Feel free to modify this
    ```
    Note: This institute email and password in the .env file will be used to login as Institute inside the app.

### Running the project

1. Open a terminal anywhere and start the Ganache blockchain.
    ```
    ganache-cli -h 127.0.0.1 -p 8545
    ```

2. Open a new terminal in the project's root directory and execute the following command to compile and deploy the smart contracts.
    ```sh
    truffle migrate
    ```

3. Change the working directory to application directory inside the project's root directory.
    ```sh
    cd application
    ```

4. Launch the streamlit app.
    ```sh
    streamlit run app.py
    ```

5. You can now view the app on your browser running on [localhost:8501](https:localhost:8501).

6. To stop the application, press Ctrl+C.

---


## Using Docker

### Prerequisites

- **Docker** 
You can either download [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows/Mac/Linux or on Linux you can install the docker package via a package manager.

### Running the project

1. Start the Docker engine by running the Docker Desktop application.

2. Open a terminal in the project's root directory.

3. Run the following command to start the 2 containers (ganache and streamlit-app).
    ```sh
    docker-compose up
    ```

4. You can now view the app on your browser running on [localhost:8501](https:localhost:8501).

5. To stop and remove the containers, use the command:
    ```sh
    docker-compose down
    ```

    Note: The insitute email id is "institute@gmail.com" and password is "123456". You will require this for logging in as Institute for the process of Certificate generation.

---

## Additional Notes

- The docker-compose.yml file provided first downloads the images for ganache and streamlit-app from Docker hub and then starts these containers using docker-compose up.

- If you want to build your own images, I have provided the Dockerfiles for ganache (Dockerfile.ganache) and streamlit-app (Dockerfile.streamlit). Before building the images, first make the below changes in application/connection.py and truffle-config.js:

    In **application/connection.py**, on line 6:
    ```
    w3 = Web3(Web3.HTTPProvider('http://ganache:8545'))
    ```
    
    In **truffle-config.js**, on line 4:
    ```
    host: "ganache",
    ```

    This changes the host to "ganache" which is the service defined in docker-compose.yml.

    After making these changes, you can build the images using `docker-compose build`. After this, you can use `docker-compose up` to start the containers and `docker-compose down` to stop them.

---

## Application Screenshots

![Home page](https://github.com/Sahil181045/Certificate-Validation-System/assets/115214968/b808b951-0e1d-479f-a891-621f0fbb374c)
<p align="center"><em>Home Page</em></p>
<br></br>

![Login page](https://github.com/Sahil181045/Certificate-Validation-System/assets/115214968/24854c98-9bc3-47eb-a84d-11cf7547812e)
<p align="center"><em>Login Page</em></p>
<br></br>

![Generate Certificate Page](https://github.com/Sahil181045/Certificate-Validation-System/assets/115214968/20b1459c-b5f6-4166-8403-d03b247c061f)
<p align="center"><em>Generate Certificate Page</em></p>
<br></br>

![View Certificate Page](https://github.com/Sahil181045/Certificate-Validation-System/assets/115214968/fca1a552-5a2d-4870-b9d9-5589da7d1fe4)
<p align="center"><em>View Certificate Page</em></p>
<br></br>

![Verify Certificate using Certificate ID](https://github.com/Sahil181045/Certificate-Validation-System/assets/115214968/cd1e91f1-61d8-439b-a486-07a9147d714f)
<p align="center"><em>Verify Certificate using Certificate ID</em></p>
<br></br>

![Verify Certificate using Certificate PDF](https://github.com/Sahil181045/Certificate-Validation-System/assets/115214968/11dc4300-3601-4f15-a801-53134e1756fd)
<p align="center"><em>Verify Certificate using Certificate PDF</em></p>
<br></br>

---

## License

This project is licensed under the MIT license. See the [LICENSE](https://github.com/Sahil181045/Certificate-Validation-System/blob/main/LICENSE) file for more details.

---
