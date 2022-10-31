def postLink(post, prefix='https://vk.com/wall'):
    return f'{prefix}{str(post.social.value)}_{post.id_post}'
