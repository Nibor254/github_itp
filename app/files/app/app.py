        # Save the file to the specified directory
        file.save(file_path)

        # Redirect to the home page after upload is successful
        return redirect("/")

    # If the method of the request is GET, show an upload form to the user
    return render_template("message.html", message="Upload your photos.")


# Define route for the preview page that accepts a dynamic 'name' parameter in the URL
@app.route("/preview/<imgname>")
def preview(imgname):
    return render_template("preview.html", name=imgname)


# Assuming 'preview' end-point exists to show the uploaded image to the user
@app.route("/download/<imgname>")
def download(imgname):
    return send_from_directory(app.config["UPLOAD_FOLDER"], imgname, as_attachment=True)


# Define a route to serve static files. For example, images, CSS, JavaScript, etc.
@app.route("/static/<name>")
def get_static(name):
    return send_from_directory("static", name)


# To keep the application running
# Define route to delete an image
@app.route("/delete/<imgname>", methods=["POST"])
def delete_image(imgname):
"""
Delete an image from the filesystem.
Redirects to home page after deletion.
"""
# Sanitize filename to prevent path traversal attacks
fname = secure_filename(imgname)
file_path = join(app.config["UPLOAD_FOLDER"], fname)
# Delete file from filesystem if it exists
try:
if exists(file_path):
os.remove(file_path)

print(f"Deleted: {fname}", file=sys.stdout)
else:
print(f"File not found: {fname}", file=sys.stderr)
except OSError as err:
print(f"Filesystem error: {err}", file=sys.stderr)
return redirect("/")
if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')