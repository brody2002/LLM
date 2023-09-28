
import cohere
from cohere.responses.classify import Example

co = cohere.Client("51F5llrM1i81Mp4A2HJ0TpApR4FF9Lpn12Nc90pN") 

examples=[
    # TOTALLY MADE UP INFORMATION JUST FOR THE FUN OF IT
    Example("1 years old.. Male", "Doesn't watch Naruto"),
    Example("2 years old. Male", "Doesn't watch Naruto"),
    Example("3 years old. Male", "Doesn't watch Naruto"),

    Example("9 years old. Male", "Does watch Naruto"),
    Example("10 years old. Male", "Does watch Naruto"),
    Example("11 years old. Male", "Does watch Naruto"),
    Example("12 years old. Male", "Does watch Naruto"),
    Example("13 years old. Male", "Does watch Naruto"),
    Example("14 years old. Male", "Does watch Naruto"),
    Example("15 years old. Male", "Does watch Naruto"),
    Example("16 years old. Male", "Does watch Naruto"),
    Example("17 years old. Male", "Does watch Naruto"),
    Example("19 years old. Male", "Does watch Naruto"),
    Example("21 years old. Male", "Does watch Naruto"),
    Example("22 years old. Male", "Does watch Naruto"),
    Example("25 years old. Male", "Does watch Naruto"),
    Example("26 years old. Male", "Does watch Naruto"),
    Example("28 years old. Male", "Does watch Naruto"),


    Example("30 years old. Male", "Doesn't watch Naruto"),
    Example("31 years old. Male", "Doesn't watch Naruto"),
    Example("33 years old. Male", "Doesn't watch Naruto"),
    Example("34 years old. Male", "Doesn't watch Naruto"),
    Example("35 years old. Male", "Doesn't watch Naruto"),
    Example("36 years old. Male", "Does watch Naruto"),
    Example("37 years old. Male", "Doesn't watch Naruto"),
    Example("35 years old. Male", "Doesn't watch Naruto"),
    Example("38 years old. Male", "Doesn't watch Naruto"),
    Example("40 years old. Male", "Doesn't watch Naruto"),
    Example("43 years old. Male", "Doesn't watch Naruto"),
    Example("54 years old. Male", "Doesn't watch Naruto"),
    Example("53 years old. Male", "Does watch Naruto"),
    Example("88 years old. Male", "Doesn't watch Naruto"),
    Example("19 years old. Male", "Doesn't watch Naruto"),

    Example("66 years old. Male", "Doesn't watch Naruto"),
    Example("88 years old. Male", "Doesn't watch Naruto"),
    Example("74 years old. Male", "Doesn't watch Naruto"),

#Female
    Example("1 years old.. Female", "Doesn't watch Naruto"),
    Example("2 years old. Female", "Doesn't watch Naruto"),
    Example("3 years old. Female", "Doesn't watch Naruto"),

    Example("9 years old. Female", "Doesn't watch Naruto"),
    Example("10 years old. Female", "Doesn't watch Naruto"),
    Example("11 years old. Female", "Doesn't watch Naruto"),
    Example("12 years old. Female", "Doesn't watch Naruto"),
    Example("13 years old. Female", "Doesn't watch Naruto"),
    Example("14 years old. Female", "Doesn't watch Naruto"),
    Example("15 years old. Female", "Doesn't watch Naruto"),
    Example("16 years old. Female", "Does watch Naruto"),
    Example("17 years old. Female", "Does watch Naruto"),
    Example("19 years old. Female", "Does watch Naruto"),
    Example("21 years old. Female", "Does watch Naruto"),
    Example("22 years old. Female", "Does watch Naruto"),
    Example("25 years old. Female", "Does watch Naruto"),
    Example("26 years old. Female", "Doesn't watch Naruto"),
    Example("28 years old. Female", "Doesn't watch Naruto"),

    Example("30 years old. Female", "Doesn't watch Naruto"),
    Example("30 years old. Female", "Does watch Naruto"),
    Example("31 years old. Female", "Doesn't watch Naruto"),
    Example("33 years old. Female", "Doesn't watch Naruto"),
    Example("34 years old. Female", "Doesn't watch Naruto"),
    Example("35 years old. Female", "Doesn't watch Naruto"),
    Example("36 years old. Female", "Doesn't watch Naruto"),
    Example("37 years old. Female", "Does watch Naruto"),
    Example("35 years old. Female", "Doesn't watch Naruto"),
    Example("38 years old. Female", "Doesn't watch Naruto"),
    Example("40 years old. Female", "Doesn't watch Naruto"),
    Example("43 years old. Female", "Doesn't watch Naruto"),
    Example("54 years old. Female", "Doesn't watch Naruto"),
    Example("53 years old. Female", "Doesn't watch Naruto"),
    Example("88 years old. Female", "Doesn't watch Naruto"),
    Example("19 years old. Female", "Doesn't watch Naruto"),

    Example("66 years old. Female", "Doesn't watch Naruto"),
    Example("88 years old. Female", "Doesn't watch Naruto"),
    Example("74 years old. Female", "Doesn't watch Naruto"),

    


    
]
inputs=[
  "17 years old. Male",
  "88 years old. Female",
  "88 years old. Male",
  "21 years old. Male",

  "22 years old. Male",
  "3 years old. Female",
  "30 years old. Male",
  "20 years old. Male",

  "77 years old. Male",
  "33 years old. Female",
  "20 years old. Female",
  "21 years old. Female",

  "1 years old. Male",
  "3 years old. Female",
  "13 years old. Male",
  "14 years old. Male",

  "15 years old. Female",
  "3 years old. Female",
  "30 years old. Male",
  "40 years old. Female",

  "23 years old. Male",
  "30 years old. Female",
  "27 years old. Female",
  "14 years old. Female",
  "40 years old. Male",
  "24 years old. Male",
  "38 years old. Male",
  "99 years old. Male",
]

response = co.classify(

  inputs=inputs,
  examples=examples,
)


for i in range(0, len(response.classifications)):
    print("INPUT: ",inputs[i]," ", response.classifications[i])

#Template changed from including only age to then including age AND gender.