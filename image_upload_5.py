import tornado.web
import tornado.ioloop
from PIL import Image, ImageOps
import model_image_matching
import gen_html

class uploadImgHandler(tornado.web.RequestHandler):
    
    def post(self):
        files = self.request.files["imgFile"]
        file = files[0]
        body = file['body']
        filename = file['filename']

        #n = self.request.form['quantity']
        #n = 5
        n = self.get_argument("quantity", "")

        with open('uploads/' + filename, 'wb') as tempfile:
          tempfile.write(body)


        imagename = "uploads/" + filename

        ###new###
        url_path = 'http://deslogin.cosmology.illinois.edu/~mcarras2/ae_data/images/'

        n = int(n) + 1
        matching_extensions = model_image_matching.get_image_names(imagename, n)
        print(matching_extensions)
        original_path = url_path + filename

        imagepaths = [url_path + matching_extensions[i] for i in range(n)]

        gen_html.gen_file(imagepaths, matching_extensions)

        self.render("current_images.html")


    def get(self):
        self.render("file_upload_form.html", name='Lauren')          

if (__name__ == "__main__"):
    settings = {'static_path' : "uploads/"}
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'uploads'})
    ], **settings)

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.instance().start()





##### only works on first time, can't figure out why
##### would love to break up into multiple functions -- would that fix problem?

