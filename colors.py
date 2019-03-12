author = { "name": "Ravish", 
            "color": "Blue",
            "shape": "circle"
}

colors = ["Green", "Blue", "Red"]

fav_colors = [ 
                { 
                    "student" : "Mary",
                    "color" : "Red"
                },
                {
                    "student" : "John",
                    "color" : "Green"
                }
        ]
if __name__ == "__main__":
    print ("The author's name is {}".format(author["name"]))
    print ("His fav color is {}".format(author["color"]))
    print ("")

    print ("The current colors are:")
    for i in colors:
        print (i)
    print ("")

new_color = input("What is your fav color?\n")
if new_color == author["color"]:
    print ("You have same fav color as {}".format(author["name"]))
    print ("")
elif new_color not in colors:
    print ("That's a new color, adding it to the list")
    colors.append(new_color)
    print ("")
    print ("There are now {} colors in the list: ".format(len(colors)))
    # message += ("The color you added was {}".format(colors[3])
    for j in colors:
        print (j)
    print ("")
else:
    pass
