$(function () {
    editormd("id_content-wmd-wrapper", {
        watch: true, // �ر�ʵʱԤ��
        lineNumbers: false,
        lineWrapping: false,
        width: "100%",
        height: 500,
        placeholder: '',
        // ���ж��mdeditorʱ��ȫ��������mdeditor��Ȼ��ʾ����������⡣
        onfullscreen: function () {
            this.editor.css("border-radius", 0).css("z-index", 9999);
        },
        onfullscreenExit: function () {
            this.editor.css({
                zIndex: 10,
                border: "1px solid rgb(221,221,221)"
            })
        },
        syncScrolling: "single",
        path: "/static/mdeditor/js/lib" + "/",
        // theme
        theme: "default",
        previewTheme: "default",
        editorTheme: "default",

        saveHTMLToTextarea: true, // editor.md ������û�в��Գɹ�
        toolbarAutoFixed: true,
        searchReplace: true,
        emoji: true,
        tex: true,
        taskList: false,
        flowChart: false,
        sequenceDiagram: true,

        // image upload
        imageUpload: true,
        imageFormats: ['jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF', 'png', 'PNG', 'bmp', 'BMP', 'webp', 'WEBP'],
        imageUploadURL: "/mdeditor/uploads/",
        toolbarIcons: function () {
            return ['undo', 'redo', '|', 'bold', 'del', 'italic', 'quote', 'ucwords', 'uppercase', 'lowercase', '|', 'h1', 'h2', 'h3', 'h5', 'h6', '|', 'list-ul', 'list-ol', 'hr', '|', 'link', 'reference-link', 'image', 'code', 'preformatted-text', 'code-block', 'table', 'datetime', 'emoji', 'html-entities', 'pagebreak', 'goto-line', '|', 'help', 'info', '||', 'preview', 'watch', 'fullscreen']
        },
        onload: function () {
            console.log('onload', this);
            //this.fullscreen();
            //this.unwatch();
            //this.watch().fullscreen();

            //this.setMarkdown("#PHP");
            //this.width("100%");
            //this.height(480);
            //this.resize("100%", 640);
        }
    });

});