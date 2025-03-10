#variables are containers to store value
#x = 5 --> integer
#y = 3.14 --> float
#z = "Ali" --> string
#is_student = True --> boolean

# typecasting = The process of converting a value of one data type to another  
#                 (string, integar, float, boolean)


# An earthling’s weight on Mars is 37.8% of their weight on Earth.
#MARS_MULTIPLE = 3.78%
#MARS_MULTIPLE = 37.8/100
MARS_MULTIPLE = 0.378



def main():
   earth_weight_str = input("Enter your weight on earth: ")
   earth_weight_float = float(earth_weight_str)
   mars_weight = earth_weight_float * MARS_MULTIPLE
   print('The equivalent weight on Mars: ' + str(mars_weight))

if __name__ == '__main__':
    main()