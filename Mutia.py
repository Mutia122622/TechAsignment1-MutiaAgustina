from flask import Flask, request, Response
import json

app = Flask(__name__)

data_sensor = []

@app.route('/sensordht/data', methods=["POST", "GET"])
def sensor():
    if request.method == 'POST':
        try:
            data = request.get_json()
            app.logger.info(f"Data diterima: {data}")
            suhu = data["suhu"]
            kelembapan = data["kelembapan"]
            waktu = data["waktu"]

            data_sensor.append({
                "suhu": suhu,
                "kelembapan": kelembapan,
                "waktu": waktu
            })

            response_data = {
                'pesan': 'Data berhasil disimpan'
            }

            response = Response(
                json.dumps(response_data),
                status=200,
                mimetype='application/json'
            )

            return response

        except Exception as e:
            app.logger.error(f"Kesalahan dalam memproses permintaan: {e}")
            response_data = {
                'pesan': 'Gagal memproses permintaan',
                'error': str(e)
            }
            response = Response(
                json.dumps(response_data),
                status=400,
                mimetype='application/json'
            )
            return response
    else:
        response_data = {
            'daftar_data_sensor': data_sensor
        }
        response = Response(
            json.dumps(response_data),
            status=200,
            mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
