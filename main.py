from pyscript import document, display

def checkName(e):
    n = document.getElementById("num1").value
    name = "Faith"
    jade_students = ["Zara Llaguno", "Jadrien Godino", "Carlos David", "Faith Benitez"]
    confirm_student = num1 in num_bers

    fname = document.getElementById("firstname").value
    lname = document.getElementById("lastname").value

    new_first_name = first_name.title()
    new_last_name = last_name.title()

    full_name = new_first_name + " " + new_last_name

    confirm_mem = full_name in club_members


    message = (f'Sorry {name}, that name is not currently in this section.🙅‍♂️' , f'Yey! {name}, this person is a proud Jadian.✅')

    document.getElementById("output1").innerHTML = message[confirm_num]

