import http.server
import ssl
import socket

class HSTSHandler(http.server.SimpleHTTPRequestHandler):
	def end_headers(self):
		# header hsts
		self.send_header("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
		# header tambahan
		self.send_header("X-Content-Type-Options", "nosniff")
		super().end_headers()

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# server
server_address = ('0.0.0.0', 443)
httpd = http.server.HTTPServer(server_address, HSTSHandler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Menjalankan web HTTPS dengan HSTS pada https://0.0.0.0:443/")
httpd.serve_forever()
