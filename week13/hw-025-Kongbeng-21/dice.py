import random
class Dice:
    def __init__(self, probabilities: list):    
        if not probabilities:
            raise ValueError("Probabilities list cannot be empty.")
        if any(p < 0 for p in probabilities):
            raise ValueError("All probabilities must be non-negative.")
        total = sum(probabilities)
        if not abs(total - 1.0) < 1e-6:
            raise ValueError(f"Probabilities must sum to 1.0, got {total:.6f}")
 
        self.probabilities = probabilities
        self.num_faces = len(probabilities)
        self.faces = list(range(1, self.num_faces + 1))
        
    def roll(self) -> int:
        return random.choices(self.faces, weights=self.probabilities, k=1)[0]
 
    def roll_many(self, n: int) -> list:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Number of rolls must be a positive integer.")
        return random.choices(self.faces, weights=self.probabilities, k=n)
 
    def __repr__(self):
        return f"Dice(faces={self.num_faces}, probabilities={self.probabilities})"
    
if __name__ == "__main__":
    probs = [0.1, 0.2, 0.3, 0.1, 0.2, 0.1]
    dice = Dice(probs)
    print("Dice:", dice)
    print("Single roll:", dice.roll())
    print("10 rolls:", dice.roll_many(10))