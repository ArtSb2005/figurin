
async function getInstagramPictures (profileName) {
	const myImage = document.querySelector('#myImage');
	const jsonDataUrl = `https://www.instagram.com/${profileName}/?__a=1`;
	const response = await fetch(jsonDataUrl);
	const jsonData = await response.json();
	const pictures = jsonData.graphql.user.edge_owner_to_timeline_media.edges;

	if (response.ok) {
		return pictures;
	} else {
		throw new Error(pictures);
	}
}


function getStaticPictures() {
	console.log('saved', data1.map(el => el.node.id));
	for (let i = 0; i < data1.length; i++) {
		$('<li class="instaItems__single"><img class="instaItems__single-image" src="' + data1[i].node.display_url + '" alt=""><div class="instaItems__single-announce"><div><p>' + data1[i].node.edge_media_to_caption.edges[0].node.text.split('#')[0].split('').map(el => el.charCodeAt(0) === 10 ? '<br>' : el).join('') + '</p><a href="item.html?id='+i+'">&hellip;Далее</a></div></div></li>').appendTo('.instaItems');
	}
	
	$('.instaItems__single-announce p + span').click(function() {
	  $('.instaItems__single').removeClass('selected');		
	  $('.instaItems__single-gallery').removeClass('visible');
		$(this).closest('.instaItems__single-announce').next().addClass('visible');
		$(this).closest('.instaItems__single').addClass('selected');
	});
	
	const pageUrl = window.location.href;
	if (pageUrl.indexOf('item') !== -1) {
		const pageId = pageUrl.split('id=')[1];
		$('.instaItemSingle__text-block2').html(data1[pageId].node.edge_media_to_caption.edges[0].node.text.split('#')[0].split('').map(el => el.charCodeAt(0) === 10 ? '<br>' : el).join(''));
		const galleryArray = data1[pageId].node.edge_sidecar_to_children.edges;
		$('<img src="'+ galleryArray[0].node.display_url +'" alt="">').prependTo($('.instaItemSingle__text-block1'));
		for (let i = 1; i < galleryArray.length; i++) {
			$('<div><img src="'+ galleryArray[i].node.display_url +'" alt=""></div>').appendTo($('.instaItemSingle__gallery'));
			$('<li>'+i+'</li>').appendTo($('.instaItemSingle__text-block1 ul'));
		}
		
		$('.instaItemSingle__gallery div img').click(function() {
			const currentUrl = $(this).attr('src');
			$('.instaItemSingle__text-block1 img').attr('src', currentUrl);
		});
		
		$('.instaItemSingle__text-block1 ul li').each(function(index) {
			$(this).click(function() {
				$('.instaItemSingle__text-block1 ul li').removeClass();
				$(this).addClass('active');
				$('.instaItemSingle__text-block1 img').attr('src', galleryArray[index].node.display_url);
			});
		});
		
		$('.instaItemSingle__text-block1 ul li:first-child').click();
	}
	
	$('.instaItems__single:not("weird1"):not("weird2")').each(function(index) {
		const desc = data1[index].node.edge_media_to_caption.edges[0].node.text;
		if (desc.indexOf('#figurina_вналичии') === -1) {
			$(this).addClass('itemSold');
		}
	});

	if (pageUrl.indexOf('stock') !== -1) {
		$('.itemSold').remove();
	}
	
	$(`<li class="instaItems__single weird1"><img src="img/pic550.png" alt=""></li>`).insertAfter('.instaItems__single:nth-child(2)');
	
	$(document).click(function() {
		$('.instaItems__single-gallery').removeClass('visible');						   
		$('.instaItems__single').removeClass('selected');		
	});
	
	$('.instaItems__single-gallery, .instaItems__single-announce p + span').click(function(e) {
		e.stopPropagation();					 
	});
		
	$(document).on('click', '.menuTrigger', function() {
		$('.menu').slideToggle();
	});
	
	$(document).on('click', '.top__logo', function() {
		window.location.href = '/index.html';
	});
}


getInstagramPictures("figurina_nao_lladro")
  .then(pictures => {
	console.log("pictures:", pictures);
	console.log(JSON.stringify(pictures));
	// console.log('received', pictures.map(el => el.node.id));
  })
  .catch(error => console.error("Error:", error));
  
$(document).ready(function() {
	$('.container__commons').load('top.inc');
	getStaticPictures();
});