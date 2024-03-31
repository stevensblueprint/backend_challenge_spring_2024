At any point in this readme, if you see something that looks <like this>, you do not include the angle braces (<>) and should instead populate the space with a value that corresponds to the short description provided.

Start by defining your database:
	docker run --name <server name> -e POSTGRES_PASSWORD=<your password> -d postgres

Any time you want to start the database again, you use the following command: 
	docker start <server name>

Use the following command to find the IP address of the database (NOT TO BE CONFUSED WITH THE GATEWAY):
	docker inspect <server name>

Use the following command to start the database client:
	docker run -it --rm postgres psql -h <IP address of database> -U postgres
Enter the password you set when prompted.

Create the primary table using the following code:
	CREATE TABLE volunteers (
				volunteer_id UUID,
				first_name VARCHAR(255),
				last_name VARCHAR(255),
				email VARCHAR(255),
				phone_number VARCHAR(255),
				date_of_birth DATE,
				address VARCHAR(255),
				skills VARCHAR(255),
				availability VARCHAR(255),
				date_joined DATE,
				background_check BOOLEAN,
				attended_events VARCHAR(255)
				);
Type \q to quit after inputting the command.

Optionally, if you want to utilize the event capabilities, you need to create a second table to handle that:
	CREATE TABLE events (
				event_id UUID,
				events VARCHAR(255)
				);

Modify line in the Config class in run.py:
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:<your password>@<IP address of database>"

Create the flask docker container:
	docker build -t cmarotti-app .

Run the flask docker container:
	docker run -p 5000:5000 --rm cmarotti-app

Now, you can send queries to the database through the IP address and port directly (utilizing an application such as Postman) such as:
	http://<IP address of database>:5000/api/volunteers/
