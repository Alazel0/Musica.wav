$(document).ready(function(){
    $('.category_list .category_item[category="all"]').addClass('ct_item-active');
    $('.category_item').click(function(){
        var catMusik = $(this).attr('category');

        $('.category_item').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        $('.musik-item .container mt-5').css('transform', 'scale(0)');
        function hideMusik(){
            $('.musik-item .container mt-5').hide();
        } setTimeout(hideMusik,400);

        function showMusik(){
            $('.musik-item .container mt-5[category="'+catMusik+'"]').show();
            $('.musik-item .container mt-5[category="'+catMusik+'"]').css('transform', 'scale(1)');
        } setTimeout(showMusik,400);
    });
    $('.category_item[category="all"]').click(function(){
        function showAll(){
            $('.musik-item .container mt-5').show();
            $('.musik-item .container mt-5').css('transform', 'scale(1)');
        } setTimeout(showAll,400);
    });
});