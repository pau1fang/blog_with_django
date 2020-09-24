// 加载 modal
function load_modal(article_id, comment_id) {
    let modal_body = '#modal_body_' + comment_id;
    let modal_id = '#comment_' + comment_id;

    // 加载编辑器
    if ($(modal_body).children().length === 0) {
        let content = '<iframe src="/comments/post-comment/' +
            article_id +
            '/' +
            comment_id +
            '"' +
            ' frameborder="0" style="width: 100%; height: 100%;" id="iframe_' +
            comment_id +
            '"></iframe>';
        $(modal_body).append(content);
    };

    $(modal_id).modal('show');
}