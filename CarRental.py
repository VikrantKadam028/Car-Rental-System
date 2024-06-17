class Vehicle():
    def __init__(self,type,model,reg_no):
        self.type = type
        self.model = model
        self.reg_no = reg_no
        self.is_rented = False
    def __str__(self):
        return(f"Type :{self.type}\nModel :{self.model}\nReg no. :{self.reg_no}")

class Car(Vehicle):
    def __init__(self,model,reg_no,num_doors ):
        super().__init__('Car',model,reg_no)
        self.num_doors = num_doors
    def __str__(self):
        return(f"Car :{self.model}\nReg no. :{self.reg_no}\nDoors :{self.num_doors}")

class Bike(Vehicle):
    def __init__(self,model,reg_no,bike):
        super().__init__('Bike',model,reg_no)
        self.bike = bike
    def __str__(self):
        return(f"Bike :{self.model}\nReg no. :{self.reg_no}\nType :{self.bike} Bike")    

class Rental():
    def __init__(self):
        self.vehicles = []
        self.rentals = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)    

    def rent_vehicle(self,customer,p_no,reg_no,rental_time):
        for vehicle in self.vehicles:
            if vehicle.reg_no == reg_no and not vehicle.is_rented:
                vehicle.is_rented = True
                rental_record = {
                    'reg_no' : reg_no,
                    'customer' : customer,
                    'rental period' : rental_time
                }
                self.rentals.append(rental_record)
                print(f"Vehicle {reg_no} is rented to {customer} for {rental_time} days.")
                return
        print(f"Vehicle {reg_no} is not avaliable for rent.")

    def return_vehicle(self,reg_no):
        for vehicle in self.vehicles:
            if vehicle.reg_no == reg_no and vehicle.is_rented:
                vehicle.is_rented = False
                print(f"Vehicle {reg_no} has been returned!")
                return
        print(f"Vehicle {reg_no} is not currently rented.")

    def get_vehicles(self,vehicle_type= None):
        avaliable_vehicles = []

        for vehicle in self.vehicles:
            if not vehicle.is_rented:
                if vehicle_type is None or vehicle.type == vehicle_type:
                    avaliable_vehicles.append(vehicle)
        return avaliable_vehicles            

       
    def display_vehicles(self,vehicles):
        if not vehicles:
            print("No vehicles avaliable.")
        else:
            for vehicle in vehicles:
                print(vehicle)    


def main():
    rental_system = Rental()
    print("************************")
    print("WELCOME TO CAR RENTAL'S")
    print("************************")
    
    while True:
        print()
        print("1.Add Vehicle\n2.Rent Vehicle\n3.Return Vehicle\n4.View Avaliable Vehicles\n5.Exit")
        choice = int(input("Enter your choice :"))

        if(choice == 1):
            vehicle_type = input("Enter the vehicle type (Car/Bike) :")
            model = input("Enter the model name :")
            reg_no = input("Enter the registration number :")
            if vehicle_type == "Car":
                num_doors = int(input("Enter the no of doors :"))
                vehicle = Car(model,reg_no,num_doors)
            elif vehicle_type == "Bike":
                bike = input("Enter the bike type (Mountain/Road) :")
                vehicle = Bike(model,reg_no,bike)
            else:
                print("Invalid vehicle type")
                continue     
            rental_system.add_vehicle(vehicle)
            print("Vehicle added successfully!!")

        elif(choice==2):
            reg_no = input("Enter the registration number :")
            customer = input("Enter your name :")
            p_no = input("Enter your p.no :")
            rental_time = int(input("Enter the rental period (in days) :"))
            rental_system.rent_vehicle(customer,p_no,reg_no,rental_time)

        elif(choice==3):
            reg_no = input("Enter the registration number :")
            rental_system.return_vehicle(reg_no)

        elif(choice==4):
            vehicle = input("Enter vehicle type to view (Car/Bike/All) :")
            if vehicle == "All":
                vehicles = rental_system.get_vehicles()
            else:
                vehicles = rental_system.get_vehicles(vehicle)
            rental_system.display_vehicles(vehicles)
        elif(choice==5):
            print("Visit again...! :)")
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()                    



