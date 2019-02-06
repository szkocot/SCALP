<script>
$(function(){

	$('body > .container').infinitescroll({
		navSelector  : "div.pagination",
		nextSelector : "div.pagination a:last",
		itemSelector : "div.item",
		bufferPx: 1000,
	});

});
</script>