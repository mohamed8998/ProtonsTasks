import math
def main():

    first_x = float(input("Enter the x part of the coordinate: "))
    first_y = float(input("Enter the y part of the coordinate: "))
    
    prev_x, prev_y = first_x, first_y
    perimeter = 0

    while True:
      x_input = input("Enter the x part of the coordinate: (blank to quit) ")
      if x_input == "":
          break
      y_input = input("Enter the y part of the coordinate: ")
        
      x = float(x_input)
      y = float(y_input)
      
      perimeter += math.dist((prev_x, prev_y), (x, y))
      x_prev, y_prev = x, y
      perimeter += math.dist((prev_x, prev_y), (first_x, first_y))

    print(f"The perimeter of that polygon is {perimeter:.5f}")

if __name__ == "__main__":
    main()
