# dog_shelter
Dog Shelter Questions

Was the left over amount intended to be subtracted prior to calculating the 20% buffer?

When I was writing the function for this project, I noticed the example provided processed the data in an unexpected way. In order to get the result in the example, I had to subtract the left over food before calculating the 20% buffer. This wouldn't actually result in a 20% buffer, and would behave strangely in situations where there is already enough food, or more than enough food left over.

I took it upon myself to write the function so it calculates the 20% food buffer prior to subtracting the left over amount. There are a couple of test scenarios added to cover the situation where the left over is enough food or more than enough food for the next month.

If this were a real life situation, I would of course have talked it over with a Dev and BA to ensure we were properly applying the 20% buffer. If the example had been determined to be the intended way, I would have kept it as is.

