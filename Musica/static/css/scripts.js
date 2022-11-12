$(document).ready(function(){
    $('.category_list .category_item[category="all"]').addClass('ct_item-active');
    $('.category_item').click(function(){
        var catMusik = $(this).attr('category');

        $('.category_item').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        $('.musik-item').css('transform', 'scale(0)');
        function hideMusik(){
            $('.musik-item').hide();
        } setTimeout(hideMusik,400)

        function showMusik(){
            $('.musik-item[category="'+catMusik+'"]').show();
            $('.musik-item[category="'+catMusik+'"]').css('transform', 'scale(1)');
        } setTimeout(showMusik,400)
    });
    $('.category_item[category="all"]').click(function(){
        $('.musik-item').show();
    });
});