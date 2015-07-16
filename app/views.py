from app import app,models
from flask import render_template,jsonify
from server import Echo

@app.route('/')
def index():
	return "Hello"
	
@app.route('/ESP', methods = ['GET','POST'])
def func():
	if request.method == 'GET':
		power = request.args.get('power','')
		IP = request.environ['REMOTE_ADDR']
		Device = models.Device.query.filter_by(device_ip = IP).first()
		if not Device:
			temp = models.Device(device_ip = IP)
			db.session.add(temp)
			db.session.commit()
			tempreading = models.Reading(Power = int(power))
			Readings = temp.readings
			Readings.append(tempreading)
			db.session.add(temp )
			db.session.commit()
		else:
			temp = models.Reading(Power = int(power))
			Readings = Device.readings
			Readings.append(temp)
			db.session.add(Device)
			db.session.commit()
	return "Added device."
	
@app.route('/list',methods=['GET','POST'])
def list():
	return jsonify(list = [i.serialize for i in models.Reading.query.all()])
	
@app.route('/chart')
def chart():
	#readings = models.Reading.query.all()
	#for i in range(len(readings)):
	#	readings[i] = readings[i].as_dict()
	#return render_template('live-server.html',list = readings)
	return render_template('live-server.html')
	
@app.route('/echo')
