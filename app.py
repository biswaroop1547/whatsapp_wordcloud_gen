from flask import Flask, render_template, request, url_for, send_file, after_this_request
# from werkzeug import secure_filename
from wordcloud_script import wordcloud
import shutil

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    # projectpath = request.form['projectFilepath']
    if request.method == 'POST':
        file = request.files['projectFilepath']
        # filename = secure_filename(file.filename)
        foldername, filename = wordcloud(file)
        

    @after_this_request
    def remove_file(response):
        try:
            shutil.rmtree(foldername)
        except Exception as error:
            print("cannot remove dir")
        
        return response
        # file_content = file.read()
    # file = request.form.get('projectFilepath')
    return send_file(foldername + '/' + filename, as_attachment=True)



if __name__ == '__main__':
    app.run(threaded=True)