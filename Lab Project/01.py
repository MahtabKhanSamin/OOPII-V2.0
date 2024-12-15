from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def verify_password(self, password):
        return self.__password == password

    def get_username(self):
        return self.__username

    @abstractmethod
    def display_panel(self):
        pass


class Person:
    def __init__(self, person_id, name, age, contact):
        self.__person_id = person_id
        self.__name = name
        self.__age = age
        self.__contact = contact

    def get_person_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_contact(self):
        return self.__contact

    def display(self):
        return f"ID: {self.__person_id}, Name: {self.__name}, Age: {self.__age}, Contact: {self.__contact}"


class Doctor(Person):
    def __init__(self, person_id, name, age, contact, specialization):
        super().__init__(person_id, name, age, contact)
        self.__specialization = specialization
        self.__appointments = []

    def schedule_appointment(self, patient, time, bill_amount):
        self.__appointments.append((patient, time))
        patient.add_treatment_cost(bill_amount)
        return f"Appointment scheduled with {patient.get_name()} at {time} with a bill of ${bill_amount}."

    def view_appointments(self):
        if not self.__appointments:
            return "No appointments scheduled."
        return "\n".join([f"Patient: {appt[0].get_name()}, Time: {appt[1]}" for appt in self.__appointments])

    def display(self):
        return super().display() + f", Specialization: {self.__specialization}"


class Patient(Person):
    def __init__(self, person_id, name, age, contact):
        super().__init__(person_id, name, age, contact)
        self.__medical_history = []
        self.__bill = 0.0

    def get_bill(self):
        return self.__bill

    def add_medical_record(self, record):
        self.__medical_history.append(record)

    def add_treatment_cost(self, cost):
        self.__bill += cost

    def view_medical_history(self):
        if not self.__medical_history:
            return "No medical history available."
        return "\n".join(self.__medical_history)

    def display(self):
        return super().display() + f", Bill: ${self.__bill}"


class AdminUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.__doctors = {}
        self.__patients = {}

    def add_doctor(self, doctor):
        if doctor.get_person_id() in self.__doctors:
            raise ValueError("Doctor ID already exists.")
        self.__doctors[doctor.get_person_id()] = doctor
        return f"Doctor {doctor.get_name()} added successfully."

    def add_patient(self, patient):
        if patient.get_person_id() in self.__patients:
            raise ValueError("Patient ID already exists.")
        self.__patients[patient.get_person_id()] = patient
        return f"Patient {patient.get_name()} added successfully."

    def view_doctors(self):
        if not self.__doctors:
            return "No doctors found."
        return "\n".join([doctor.display() for doctor in self.__doctors.values()])

    def view_patients(self):
        if not self.__patients:
            return "No patients found."
        return "\n".join([patient.display() for patient in self.__patients.values()])

    def schedule_appointment(self, doctor_id, patient_id, time, bill_amount):
        if doctor_id not in self.__doctors:
            raise KeyError("Doctor ID not found.")
        if patient_id not in self.__patients:
            raise KeyError("Patient ID not found.")
        doctor = self.__doctors[doctor_id]
        patient = self.__patients[patient_id]
        return doctor.schedule_appointment(patient, time, bill_amount)

    def display_panel(self):
        while True:
            print("\nAdmin Panel")
            print("1. Add Doctor")
            print("2. Add Patient")
            print("3. View Doctors")
            print("4. View Patients")
            print("5. Schedule Appointment")
            print("6. Logout")
            admin_choice = input("Choose an option: ")

            if admin_choice == "1":
                doc_id = int(input("Doctor ID: "))
                name = input("Name: ")
                age = int(input("Age: "))
                contact = input("Contact: ")
                specialization = input("Specialization: ")
                doctor = Doctor(doc_id, name, age, contact, specialization)
                try:
                    print(self.add_doctor(doctor))
                except ValueError as e:
                    print(e)

            elif admin_choice == "2":
                pat_id = int(input("Patient ID: "))
                name = input("Name: ")
                age = int(input("Age: "))
                contact = input("Contact: ")
                patient = Patient(pat_id, name, age, contact)
                try:
                    print(self.add_patient(patient))
                except ValueError as e:
                    print(e)

            elif admin_choice == "3":
                print(self.view_doctors())

            elif admin_choice == "4":
                print(self.view_patients())

            elif admin_choice == "5":
                doc_id = int(input("Doctor ID: "))
                pat_id = int(input("Patient ID: "))
                time = input("Appointment Time: ")
                bill = float(input("Bill Amount: "))
                try:
                    print(self.schedule_appointment(doc_id, pat_id, time, bill))
                except KeyError as e:
                    print(e)

            elif admin_choice == "6":
                print("Logging out...")
                break

            else:
                print("Invalid choice.")


class HospitalSystem:
    def __init__(self):
        self.__users = {}

    def add_user(self, username, password, user_type):
        if username in self.__users:
            raise ValueError("Username already exists.")
        if user_type == "admin":
            self.__users[username] = AdminUser(username, password)
        else:
            raise ValueError("Invalid user type.")

    def login(self, username, password):
        if username not in self.__users:
            return None, "Username not found."
        user = self.__users[username]
        if not user.verify_password(password):
            return None, "Incorrect password."
        return user, f"Welcome {username}!"

    def sign_up(self, username, password):
        if username in self.__users:
            raise ValueError("Username already exists.")
        self.__users[username] = AdminUser(username, password)  # Default to AdminUser for simplicity
        print(f"User {username} signed up successfully.")


def main():
    hospital_system = HospitalSystem()

    # Predefined admin account
    hospital_system.add_user("admin", "1234", "admin")

    while True:
        print("\n***** Hospital Management System *****")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            user, message = hospital_system.login(username, password)
            print(message)

            if user:
                user.display_panel()

        elif choice == "2":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            try:
                hospital_system.sign_up(username, password)
            except ValueError as e:
                print(e)

        elif choice == "3":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()