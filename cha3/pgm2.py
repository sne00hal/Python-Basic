letter = ''' Dear <|Name|>,
You are Selected!

Date: <|DATE|>
'''
name = input("Enter your name \n");
date = input("Enter Date \n");
letter=letter.replace("<|Name|>", name);
letter=letter.replace("<|DATE|>", date);
print(letter);
