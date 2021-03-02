
class DogShelter:
    MAX_COUNT = 30
    FOOD_BUFFER = .20
    SMALL_FOOD = 10
    MEDIUM_FOOD = 20
    LARGE_FOOD = 30

    @classmethod
    def get_food_quantity(cls, small: float, medium: float, large: float, left_over: float):
        if small + medium + large > cls.MAX_COUNT:
            raise ValueError(f'{small} + {medium} + {large} is more than the {cls.MAX_COUNT} '
                             f'maximum dog count the shelter can hold')

        if small < 0:
            raise ValueError('small dog count must be 0 or greater')
        elif medium < 0:
            raise ValueError('medium dog count must be 0 or greater')
        elif large < 0:
            raise ValueError('large dog count must be 0 or greater')

        if left_over < 0:
            raise ValueError('left over food must be 0 or greater')

        # The example for this function was calculating the 20% food buffer after subtracting the left over amount
        # Doing so produces an incorrect amount of food, which becomes more apparent when there is a lot left over
        # This method has been adjusted to properly produce the required amount of food plus a 20% buffer
        min_food = small * cls.SMALL_FOOD + medium * cls.MEDIUM_FOOD + large * cls.LARGE_FOOD
        min_food_buffer = min_food * cls.FOOD_BUFFER
        min_food_total = min_food + min_food_buffer
        total_food_required = min_food_total - left_over

        return total_food_required
