# car CRUD operations with database connectivity
import mysql.connector as c

 # create connection
con = c.connect(host="localhost",user="root",passwd="root",database="car_dekho_python")
cursor = con.cursor()
 # if(con.is_connected):
        #      print("connection successfully created....")
        # else:
        #      print("due to some error connection failed..")  
        

# insert car details..........................
def insert(id,name,color,brand,fuel_type,price):
        query = "Insert into car_details values ({},'{}','{}','{}','{}',{})".format(id,name,color,brand,fuel_type,price);
        cursor.execute(query)
        print("insertion successfully done..✔")
        getAllDetails()
        con.commit()
        
#update car details............... 
def update(id):
        query=""
        update_op = input("----------What you want to update------------\nEnter 1 for update id\nEnter 2 for update Name\nEnter 3 for update color\nEnter 4 for update brand\nEnter 5 for update fuel type\nEnter 6 for update price")
        if(update_op == "1"):
             new_id = int(input("Enter new id: "))
             query = "Update car_details set id={} where id={}".format(new_id,id)
        elif(update_op=="2"):
            new_name = input("Enter new name: ")
            query = "Update car_details set name='{}' where id={}".format(new_name,id)
        elif(update_op =="3"):
            new_color = input("Enter new color: ")
            query = "Update car_details set color='{}' where id={}".format(new_color,id)
        elif(update_op =="4"):
           new_brand = input("Enter new brand: ")
           query = "Update car_details set brand='{}' where id={}".format(new_brand,id)
        elif(update_op=="5"):
            new_fuelType = input("Enter new fuel type: ")
            query = "Update car_details set fuel_Type='{}' where id={}".format(new_fuelType,id)
        elif(update_op=="6"):
            new_price = int(input("Enter new price: "))
            query = "Update car_details set price={} where id={}".format(new_price,id)
        else:
            print("Thank you!")
     
        cursor.execute(query)
        if(cursor.rowcount>0):
         print("updation successfully done..")
         getAllDetails()
        else:
         print("Invalid id, updation not possible")
        con.commit() 
   
   
# remove car details by id
def remove(id):
    query = "delete from car_details where id={}".format(id)
    cursor.execute(query)
    if(cursor.rowcount>0):
        print("car details has been removed successfully ✔")
        getAllDetails()
    else:
        print("invalid id.......deletion not performed ❌")
    con.commit()
    
    

# get all car records
def getAllDetails():
    query = "select * from car_details"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    

 







        
