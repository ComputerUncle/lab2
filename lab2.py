
def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 num_list = get_user_input()
 print("Num list: ",num_list)
 print ("Average is: ",calc_average(num_list))
 print ("Min Max is: ", find_min_max(num_list))
 print ("Sorted data is: ",sort_temperature(num_list))
def get_user_input():
 list = []
 n = int(input())
 for i in range (0,n):
  print ("Input value for number" , i+1)
  x = float(input())
  list.append(x)
 return list
 
def display_main_menu():
 print("display_main_menu")
 print ("Main Menu, input number of value")
def calc_average(n):
 avg = sum(n)/len(n)
 return avg

def find_min_max(n):
 list = []
 list.append(min(n))
 list.append(max(n))
 return list

def sort_temperature(n):
 list = n
 list.sort()
 return list


if __name__ == "__main__":
 main()


