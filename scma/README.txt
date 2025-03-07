------------------------------------------------------------------------------------------------------------------
Secure Copyright Management Application (SCMA)
------------------------------------------------------------------------------------------------------------------

Table of Contents

1. Introduction
2. System Requirements
3. Installation Instructions
4. Usage Guide
5. Features
6. Security Measures
7. Testing Instructions
8. Limitations
9. References
------------------------------------------------------------------------------------------------------------------
1. Introduction

The Secure Copyright Management Application (SCMA) is a command line application, 
written in Python language for the protection of intellectual property by securely storing 
and managing artefacts such as text files, documents, and audio files. Various security 
features are implemented in this python based command line application including 
AES-256 encryption, SHA-256 hashing, Role Based Access Control (RBAC), and Audit 
Logs to make sure confidentiality, integrity and authenticity of the stored artefacts.
------------------------------------------------------------------------------------------------------------------
2. System Requirements

• Python 3.x
• cryptography library
• Windows, Linux, or Mac OS
------------------------------------------------------------------------------------------------------------------
3. Installation Instructions

Prerequisites
Install Python 3 or higher version from the official website: https://www.python.org/downloads/ 
Install Required Libraries

Open your terminal or command prompt and run the following command:
pip install cryptography

Application Setup
1.	Download the SCMA application files.
2.	Extract the files into your preferred directory.
------------------------------------------------------------------------------------------------------------------
4. Usage Guide

How to Run the Application
Navigate to the application folder and execute the following command:
python scma.py

Login Credentials
Role	Username	Password
Admin	admin	admin123
User	user	user123

Main Menu Options
Option	Description		Permissions
1. Create	Upload text or file artefacts	Admin, User
2. Read	View artefact content		Admin, User
3. Update	Modify artefact content	Admin, User (Own Artefacts Only)
4. Delete	Remove artefact		Admin Only
5. Exit	Terminate the application	All Users
------------------------------------------------------------------------------------------------------------------
5. Features

• AES-256 Encryption for secure artefact storage
• SHA-256 Hashing for data integrity
• Role-Based Access Control (RBAC)
• Automatic Timestamps for artefact creation and modification
• Audit Logs for user interactions
• Text and File Artefact Support (TXT, MP3, PDF)
------------------------------------------------------------------------------------------------------------------
6. Security Measures

Security Feature	Implementation
Encryption		AES-256 using cryptography.fernet
Integrity Verification	SHA-256 hash comparison
RBAC		Admin and User Roles
Timestamping	Automated Creation/Modification Timestamps
Audit Logs		Logs stored in scma_log.txt
------------------------------------------------------------------------------------------------------------------
7. Testing Instructions

Functional Testing
Test Case			Expected Outcome		
Create Artefact (Text)		Artefact created and encrypted	
Read Artefact		Decrypted content displayed	
Update Artefact		Content updated and encrypted	
Delete Artefact (Admin)	Artefact removed	
Unauthorized Delete (User)	Action denied	

Security Testing
The application has been tested using Bandit for common security vulnerabilities. To run security tests:
pip install bandit
bandit application.py
------------------------------------------------------------------------------------------------------------------
8. Limitations
• The application currently supports only local file storage.
• No multi-user concurrent session management.
• Basic password authentication without hashing.
------------------------------------------------------------------------------------------------------------------
9. References

• Buelta, J., 2022. Python Architecture Patterns: Master API design, event-driven structures, and package 
management in Python. Packt Publishing Ltd.
• Gamma, E., Helm, R., Johnson, R. and Vlissides, J., 1995. Design patterns: elements of reusable object 
oriented software. Pearson Deutschland GmbH.
• Khan, R.A., Khan, S.U., Khan, H.U. and Ilyas, M., 2022. Systematic literature review on security risks 
and its practices in secure software development. ieee Access, 10, pp.5456-5481.
• Object Management Group (2020) Unified Architecture Framework (UAF) Domain Metamodel. 
Version 1.1. Available at: https://www.omg.org/spec/UAF/1.1 (Accessed: 2 February 2025).
• Tutorialspoint (2022) Cryptography with Python - Quick Guide. Available at: 
https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm 
(Accessed: 2 February 2025).	
------------------------------------------------------------------------------------------------------------------
				THE END
------------------------------------------------------------------------------------------------------------------