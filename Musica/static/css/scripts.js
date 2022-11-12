$(document).ready(function(){
    $('.category_list .category_item[category="all"]').addClass('ct_item-active');
    $('.category_item').click(function(){
        var catMusik = $(this).attr('category');

        $('.category_item').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        $('.musik-item').hide();

        $('.musik-item[category="'+catMusik+'"]').show();
    });
    $('.category_item[category="all"]').click(function(){
        $('musik-item').show();
    });
});