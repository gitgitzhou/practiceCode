import SocketServer
import SimpleHTTPServer

PORT = 8080
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port", PORT)

httpd.serve_forever()
