//文件上传
$(function() {
    $("#file_upload").uploadify({
        height: 30,
        removeCompleted : false,
        swf: '../static/flash/uploadify.swf',
        uploader:'../static/flash/uploadify.php',
        formData: {},
        width: 120,
        'onUploadSuccess': function(file, data, response) {
            var result = jQuery.parseJSON(data);
            alert(result.msg);
        },
    });
}); 