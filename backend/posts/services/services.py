from posts.repositories.repositories import PostRepository


class PostService:
    @staticmethod
    def get_likes_analytics(date_from, date_to):
        return PostRepository.get_likes_analytics(date_from, date_to)
