function desaturateImage(image) {
  var canvas = document.createElement('canvas');
  image.parentNode.insertBefore(canvas, image);

  canvas.width = image.width;
  canvas.height = image.height;

  var ctx = canvas.getContext("2d");
  ctx.drawImage(image, 0, 0);

  var imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);

  for (var i = 0; i < imgData.data.length; i += 4) {
    var r = imgData.data[i];
    var g = imgData.data[i + 1];
    var b = imgData.data[i + 2];

    var grey = 0.2126 * r + 0.7152 * g + 0.0722 * b;

    imgData.data[i] = grey;
    imgData.data[i + 1] = grey;
    imgData.data[i + 2] = grey;
  }

  ctx.putImageData(imgData, 0, 0);
}

window.onload = function () {
  var img = document.getElementById("myImage");
  desaturateImage(img);
};
