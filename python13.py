null_dict={}
null_dict["name"]="dictionary"
print(null_dict)

#nested Dictionaries
student={
    "name":"Rahul Kumar",
    "subjects":{
        "physics":97,
        "chemistry":98,
        "maths":70
    }
}
print(student)

print(student["subjects"]["chemistry"])
print(student["subjects"]["maths"])
print(student["subjects"]["physics"])

#dictionary Methods
#keys
print(list(student.keys()))

#length
print(len(student))

#values
print(list(student.values()))

#items
print(student.items())

#pairs
pairs=list(student.items())
print(pairs[0])
print(pairs[1])

#get
print(student.get("name"))
print(student.get("subjects"))

#update
student.update({"city":"delhi"})
print(student)
