from pyscript import document

def checkName(e):
    #to indicate who is currently in the section
    jade_students = ["Zara Llaguno", "Jadrien Godino", "Carlos David, Faith Benitez"]
    #assigning variable names to id
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = (first_name + " " + last_name).title()

    confirm_student = full_name in jade_students

    message = (
        f"Sorry {full_name}, that name is not currently in this section.🙅‍♂️",
        f"Yey! {full_name}, you a proud Jadian.✅"
    )

    document.getElementById("output1").innerText = message[confirm_student]
