import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    syncs = await bot.tree.sync()
    print(f"{len(syncs)} synced commands!")
    print("Bot Initialized!")
    print("Now Is Time to Make some Maths!")
    print(f"Bot Connected as {bot.user}")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name = "maths", description = "Makes a simple math calculation")
async def maths(interaction: discord.Interaction, expression: str):
    try:
        result = eval(expression)
        await interaction.response.send_message(f"The Result of `{expression}` is: {result}")
    except Exception as e:
        await interaction.response.send_message(f"Error calculating expression: {e}")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name = "ping", description = "Check the bot's latency")
async def ping(interaction: discord.Interaction):
    latency = bot.latency * 1000  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! Latency: {latency:.2f} ms")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="help", description="Get a list of available commands")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="Available Commands", color=discord.Color.blue())
    embed.add_field(name="/maths <expression>", value="Makes a simple math calculation.\nExample: `/maths 2 + 2 * 3`", inline=False)
    embed.add_field(name="/ping", value="Check the bot's latency.", inline=False)
    embed.add_field(name="/expert <expression>", value="Makes a more complex math calculation with math module.\nExample: `/expert sqrt(16)`", inline=False)
    embed.add_field(name="/learn <topic>", value="Learn basic math concepts.\nTopics: algebra, geometry, calculus, trigonometry", inline=False)
    embed.add_field(name="/algebra", value="Learn a comprehensive guide about algebra.", inline=False)
    embed.add_field(name="/geometry", value="Learn a comprehensive guide about geometry.", inline=False)
    embed.add_field(name="/calculus", value="Learn a comprehensive guide about calculus.", inline=False)
    embed.add_field(name="/trigonometry", value="Learn a comprehensive guide about trigonometry.", inline=False)
    embed.add_field(name="/statistics", value="Learn a comprehensive guide about statistics.", inline=False)
    embed.add_field(name="/number", value="Learn a comprehensive guide about number theory.", inline=False)
    embed.add_field(name="/combinatorics", value="Learn a comprehensive guide about combinatorics.", inline=False)
    embed.add_field(name="/abstractalgebra", value="Learn a comprehensive guide about abstract algebra.", inline=False)
    embed.add_field(name="/realanalysis", value="Learn a comprehensive guide about real analysis.", inline=False)
    embed.add_field(name="/help", value="Get a list of available commands.", inline=False)
    embed.add_field(name="/ais [IN DEVELOPMENT]", value="introduce some useful AI tools to learn math", inline=False)
    embed.add_field(name="/sites", value="introduce some useful websites to learn math", inline=False)
    embed.add_field(name="/info", value="Get information about the bot.", inline=False)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name = "expert", description = "Makes a more complex math calculation")
async def expert_maths(interaction: discord.Interaction, expression: str):
    try:
        # For more complex calculations, we can use the 'math' module
        import math
        # Create a safe environment for eval
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names.update({"__builtins__": {}})
        result = eval(expression, {"__builtins__": None}, allowed_names)
        await interaction.response.send_message(f"The Result of `{expression}` is: {result}")
    except Exception as e:
        await interaction.response.send_message(f"Error calculating expression: {e}")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="learn", description="Learn some basic math concepts")
async def learn_maths(interaction: discord.Interaction, topic: str):
    topics = {
        "algebra": {
            "description": "Algebra is the branch of mathematics that uses symbols and letters to represent numbers and quantities in formulas and equations.",
            "advanced_content": "**Advanced Concepts:**\n• Polynomial rings and algebraic structures\n• Linear transformations and vector spaces\n• Eigenvalues and eigenvectors: Solve det(A - λI) = 0\n• Abstract algebra foundations for modern cryptography\n\n**Examples:**\n• Solve: 3x² + 5x - 2 = 0 → x = (-5 ± √49)/6 → x = 1/3 or x = -2\n• Matrix operations: For A = [[1,2],[3,4]], find eigenvalues\n• Systems: 2x + 3y = 8, 5x - y = 7 → x = 2, y = 4/3"
        },
        "geometry": {
            "description": "Geometry is the branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.",
            "advanced_content": "**Advanced Concepts:**\n• Differential geometry and curvature tensors\n• Non-Euclidean geometries (hyperbolic, spherical)\n• Projective geometry and homogeneous coordinates\n• Topological invariants and homology groups\n\n**Examples:**\n• Sphere volume: V = (4/3)πr³; for r=5 → V ≈ 523.6 cubic units\n• Distance in 3D: d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]\n• Hyperbolic geometry: Sum of angles in triangle < 180°\n• Curvature: κ = |dT/ds| for parametric curves"
        },
        "calculus": {
            "description": "Calculus is the branch of mathematics that studies continuous change, through derivatives and integrals.",
            "advanced_content": "**Advanced Concepts:**\n• Multivariable calculus: Partial derivatives, ∇f, and Hessian matrices\n• Vector calculus: Divergence theorem, Stokes' theorem, line integrals\n• Differential equations: Both ODEs and PDEs\n• Functional analysis and distribution theory\n\n**Examples:**\n• Derivative: f(x) = e^(x²) → f'(x) = 2xe^(x²)\n• Integral: ∫₀^π x·sin(x) dx = π (integration by parts)\n• Gradient: ∇f(x,y) = (∂f/∂x, ∂f/∂y) for f(x,y) = x²y + y³\n• Differential Eq: dy/dx + 2y = e^x → y = (e^x + Ce^(-2x))/3"
        },
        "trigonometry": {
            "description": "Trigonometry is the branch of mathematics that studies the relationships between the angles and sides of triangles.",
            "advanced_content": "**Advanced Concepts:**\n• Complex exponentials: e^(iθ) = cos(θ) + i·sin(θ) (Euler's formula)\n• Fourier analysis: Decompose periodic functions into sine/cosine series\n• Trigonometric identities in harmonic analysis\n• Applications in signal processing and quantum mechanics\n\n**Examples:**\n• Law of cosines: c² = a² + b² - 2ab·cos(C); with a=5, b=7, C=60° → c ≈ 6.24\n• Fourier series: Any periodic function f(x) = a₀/2 + Σ[aₙ·cos(nx) + bₙ·sin(nx)]\n• Complex form: e^(iπ) + 1 = 0 (Euler's identity)\n• Half-angle: sin(θ/2) = ±√[(1-cos(θ))/2]"
        }
    }
    topic = topic.lower()
    if topic in topics:
        topic_data = topics[topic]
        embed = discord.Embed(
            title=f"{topic.capitalize()} - Advanced Guide",
            description=topic_data["description"],
            color=discord.Color.blue()
        )
        embed.add_field(
            name="Advanced Insights",
            value=topic_data["advanced_content"],
            inline=False
        )
        embed.set_footer(text=f"Requested by {interaction.user.name} | Use /expert to practice")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title="Error",
            description="Sorry, I don't have information on that topic. Available topics: algebra, geometry, calculus, trigonometry",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="math_topics", description="List all available math topics to learn")
async def math_topics(interaction: discord.Interaction):
    embed = discord.Embed(title="Available Math Topics", color=discord.Color.green())
    topics_list = "algebra, geometry, calculus, trigonometry, statistics, number theory, combinatorics, abstract algebra, real analysis"
    embed.description = topics_list
    embed.set_footer(text="Use /learn <topic> to learn more")
    await interaction.response.send_message(embed=embed)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="algebra", description="Learn about algebra")
async def learn_algebra(interaction: discord.Interaction):
    embed = discord.Embed(title="Algebra - A Comprehensive Guide", color=discord.Color.purple())
    
    embed.add_field(
        name="What is Algebra?",
        value="Algebra is the branch of mathematics using symbols and letters to represent numbers in equations and formulas.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Variables and expressions\n• Constants and coefficients\n• Order of operations (PEMDAS)\n• Combining like terms\n• Distributive property",
        inline=False
    )
    
    embed.add_field(
        name="Linear Equations",
        value="• Solving for variables\n• Writing equations from word problems\n• Graphing lines\n• Slope and intercepts\n• Parallel and perpendicular lines",
        inline=False
    )
    
    embed.add_field(
        name="Quadratic Equations",
        value="• Factoring trinomials\n• Completing the square\n• Quadratic formula\n• Graphing parabolas\n• Vertex form",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Functions and transformations\n• Systems of equations\n• Inequalities and absolute values\n• Polynomial operations\n• Rational expressions",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Linear**: Solve 2x + 5 = 13 → x = 4\n**Quadratic**: x² + 5x + 6 = 0 → x = -2 or x = -3\n**Distributive**: 3(x + 2) = 3x + 6\n**Systems**: x + y = 5, x - y = 1 → x = 3, y = 2",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/algebra\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Gilbert Strang**, **Paul Zeitz**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Solve problems daily\n✓ Review foundational concepts\n✓ Practice word problems\n✓ Check your work\n✓ Understand, don't memorize",
        inline=False
    )
    
    embed.set_footer(text="Master algebra step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="geometry", description="Learn about geometry")
async def learn_geometry(interaction: discord.Interaction):
    embed = discord.Embed(title="Geometry - A Comprehensive Guide", color=discord.Color.orange())
    
    embed.add_field(
        name="What is Geometry?",
        value="Geometry is the branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Points, lines, and planes\n• Angles and their types\n• Triangles and their properties\n• Quadrilaterals and polygons\n• Circles and their properties",
        inline=False
    )
    
    embed.add_field(
        name="Solid Geometry",
        value="• Polyhedra and their properties\n• Surface area and volume calculations\n• Spheres, cylinders, and cones\n• Cross-sections of solids",
        inline=False
    )
    
    embed.add_field(
        name="Coordinate Geometry",
        value="• Cartesian coordinates\n• Distance formula\n• Midpoint formula\n• Slope of a line\n• Equations of lines and circles",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Transformations (translations, rotations, reflections)\n• Similarity and congruence\n• Trigonometry in geometry\n• Non-Euclidean geometries",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Area of Circle**: πr² with r=5 → Area = 78.54\n**Volume of Sphere**: (4/3)πr³ with r=3 → Volume = 113.1\n**Distance Formula**: √[(x₂-x₁)² + (y₂-y₁)²]\n**Pythagorean Theorem**: a² + b² = c²",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/geometry\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Euclid**, **René Descartes**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Draw diagrams to visualize problems\n✓ Practice proofs regularly\n✓ Solve a variety of problems\n✓ Review fundamental theorems\n✓ Understand concepts deeply",
        inline=False
    )
    
    embed.set_footer(text="Master geometry step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="calculus", description="Learn about calculus")
async def learn_calculus(interaction: discord.Interaction):
    embed = discord.Embed(title="Calculus - A Comprehensive Guide", color=discord.Color.red())
    
    embed.add_field(
        name="What is Calculus?",
        value="Calculus is the branch of mathematics that studies continuous change, through derivatives and integrals.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Limits and continuity\n• Derivatives and differentiation\n• Integrals and integration\n• Fundamental Theorem of Calculus\n• Applications of derivatives and integrals",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Derivatives**: Find the slope of f(x) = x² → f'(x) = 2x\n**Integrals**: ∫2x dx = x² + C\n**Limits**: lim(x→2) x² = 4",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Multivariable calculus\n• Vector calculus\n• Differential equations\n• Series and sequences\n• Real analysis",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/calculus\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Isaac Newton**, **Gottfried Wilhelm Leibniz**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Solve problems daily\n✓ Review foundational concepts\n✓ Practice word problems\n✓ Check your work\n✓ Understand, don't memorize",
        inline=False
    )
    
    embed.set_footer(text="Master calculus step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="trigonometry", description="Learn about trigonometry")
async def learn_trigonometry(interaction: discord.Interaction):
    embed = discord.Embed(title="Trigonometry - A Comprehensive Guide", color=discord.Color.yellow())
    
    embed.add_field(
        name="What is Trigonometry?",
        value="Trigonometry is the branch of mathematics that studies the relationships between the angles and sides of triangles.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Trigonometric functions (sine, cosine, tangent)\n• Inverse trigonometric functions\n• Trigonometric identities\n• Solving triangles\n• Applications in real-world problems",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Sine**: sin(30°) = 0.5\n**Cosine**: cos(60°) = 0.5\n**Tangent**: tan(45°) = 1",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Trigonometric equations\n• Inverse trigonometric functions\n• Trigonometric graphs\n• Polar coordinates\n• Complex numbers in trigonometry",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/trigonometry\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Euclid**, **Leonhard Euler**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Practice with triangles and angles\n✓ Learn identities by heart\n✓ Use calculators for complex values\n✓ Solve word problems involving triangles\n✓ Understand the unit circle",
        inline=False
    )
    
    embed.set_footer(text="Master trigonometry step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="statistics", description="Learn about statistics")
async def learn_statistics(interaction: discord.Interaction):
    embed = discord.Embed(title="Statistics - A Comprehensive Guide", color=discord.Color.green())
    
    embed.add_field(
        name="What is Statistics?",
        value="Statistics is the branch of mathematics that deals with collecting, analyzing, and interpreting data.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Descriptive statistics\n• Inferential statistics\n• Probability theory\n• Data visualization\n• Hypothesis testing",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Mean**: (2+4+6+8)/4 = 5\n**Median**: [1, 3, 5, 7] → 4\n**Standard Deviation**: σ = √(Σ(x-μ)²/N)\n**Z-Score**: z = (x-μ)/σ\n**Correlation**: r ∈ [-1, 1]",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Regression analysis\n• ANOVA (Analysis of Variance)\n• Bayesian statistics\n• Time series analysis\n• Multivariate statistics",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/statistics\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Ronald Fisher**, **Karl Pearson**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Work with real datasets\n✓ Use statistical software like R or Python (pandas, numpy)\n✓ Practice hypothesis testing problems\n✓ Visualize data using graphs and charts\n✓ Understand the assumptions behind statistical methods",
        inline=False
    )
    
    embed.set_footer(text="Master statistics step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="number", description="Learn about number theory")
async def learn_number_theory(interaction: discord.Interaction):
    embed = discord.Embed(title="Number Theory - A Comprehensive Guide", color=discord.Color.dark_blue())
    
    embed.add_field(
        name="What is Number Theory?",
        value="Number theory is the branch of mathematics that studies the properties of integers.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Divisibility and prime numbers\n• Greatest common divisor (GCD) and least common multiple (LCM)\n• Modular arithmetic\n• Diophantine equations\n• Euler's totient function",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Prime Numbers**: 2, 3, 5, 7, 11, 13\n**GCD**: GCD(12, 8) = 4\n**LCM**: LCM(12, 8) = 24\n**Modular Arithmetic**: 17 mod 5 = 2\n**Diophantine**: 3x + 5y = 1 → x=2, y=-1",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Cryptography\n• Continued fractions\n• Quadratic reciprocity\n• Elliptic curves\n• Algebraic number theory",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/number-theory\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Euclid**, **Leonhard Euler**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Learn divisibility rules and prime factorization\n✓ Practice modular arithmetic problems\n✓ Solve Diophantine equations step by step\n✓ Understand Euler's totient function and its applications\n✓ Explore applications in cryptography",
        inline=False
    )
    
    embed.set_footer(text="Master number theory step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="combinatorics", description="Learn about combinatorics")
async def learn_combinatorics(interaction: discord.Interaction):
    embed = discord.Embed(title="Combinatorics - A Comprehensive Guide", color=discord.Color.dark_green())
    
    embed.add_field(
        name="What is Combinatorics?",
        value="Combinatorics is the branch of mathematics that studies counting and arrangements.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Permutations and combinations\n• Binomial coefficients\n• Pigeonhole principle\n• Inclusion-exclusion principle\n• Generating functions",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Permutations**: P(5,3) = 5!/(5-3)! = 60\n**Combinations**: C(5,3) = 5!/(3!×2!) = 10\n**Binomial**: (x+y)³ = x³ + 3x²y + 3xy² + y³\n**Pigeonhole**: 10 pigeons, 9 holes → at least 1 hole has 2+ pigeons",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Graph theory\n• Ramsey theory\n• Design theory\n• Enumerative combinatorics\n• Probabilistic methods",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/combinatorics\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Leonhard Euler**, **Pólya**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Master basic counting principles\n✓ Practice permutation and combination problems\n✓ Learn generating functions and their applications\n✓ Explore graph theory concepts in combinatorics\n✓ Solve advanced problems in enumerative combinatorics",
        inline=False
    )
    
    embed.set_footer(text="Master combinatorics step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="abstractalgebra", description="Learn about abstract algebra")
async def learn_abstract_algebra(interaction: discord.Interaction):
    embed = discord.Embed(title="Abstract Algebra - A Comprehensive Guide", color=discord.Color.dark_red())
    
    embed.add_field(
        name="What is Abstract Algebra?",
        value="Abstract algebra is the branch of mathematics that studies algebraic structures like groups, rings, and fields.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Groups and group theory\n• Rings and ring theory\n• Fields and field theory\n• Homomorphisms and isomorphisms\n• Applications in cryptography and coding theory",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Groups**: Symmetry group of a square has 8 elements\n**Rings**: Integers under addition and multiplication form a ring\n**Fields**: Rational numbers form a field\n**Homomorphisms**: f(x) = 2x is a homomorphism from (Z, +) to (Z, +)",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Galois theory\n• Representation theory\n• Non-commutative algebra\n• Category theory\n• Algebraic geometry",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/abstract-algebra\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Évariste Galois**, **Emmy Noether**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Understand definitions and theorems deeply\n✓ Practice proving properties of algebraic structures\n✓ Explore applications in cryptography and coding theory\n✓ Solve problems in group theory, ring theory, and field theory\n✓ Study advanced topics like Galois theory for deeper insights",
        inline=False
    )
    
    embed.set_footer(text="Master abstract algebra step by step! Use /expert to test your skills.")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="realanalysis", description="Learn about real analysis")
async def learn_real_analysis(interaction: discord.Interaction):
    embed = discord.Embed(title="Real Analysis - A Comprehensive Guide", color=discord.Color.dark_orange())
    
    embed.add_field(
        name="What is Real Analysis?",
        value="Real analysis is the branch of mathematics that studies real numbers and real-valued functions.",
        inline=False
    )
    
    embed.add_field(
        name="Fundamentals",
        value="• Real numbers and their properties\n• Sequences and series\n• Continuity and limits\n• Differentiation and integration\n• Metric spaces and topology",
        inline=False
    )
    
    embed.add_field(
        name="Examples",
        value="**Limits**: lim(x→0) sin(x)/x = 1\n**Continuity**: f(x) = x² is continuous everywhere\n**Differentiation**: f'(x) = 2x for f(x) = x²\n**Integration**: ∫x dx = (1/2)x² + C",
        inline=False
    )
    
    embed.add_field(
        name="Advanced Topics",
        value="• Measure theory\n• Lebesgue integration\n• Functional analysis\n• Fourier analysis\n• Complex analysis",
        inline=False
    )
    
    embed.add_field(
        name="Learning Resources",
        value="🔗 **Khan Academy**: www.khanacademy.org/math/real-analysis\n🔗 **3Blue1Brown**: www.youtube.com/@3blue1brown\n🔗 **Paul's Online Math Notes**: tutorial.math.lamar.edu\n🔗 **Wolfram MathWorld**: mathworld.wolfram.com",
        inline=False
    )
    
    embed.add_field(
        name="Expert Recommendations",
        value="Study by **Augustin-Louis Cauchy**, **Bernhard Riemann**, and **MIT OpenCourseWare** for deep understanding.",
        inline=False
    )
    
    embed.add_field(
        name="Practice Tips",
        value="✓ Master the definitions of limits, continuity, and differentiability\n✓ Practice proving theorems in real analysis\n✓ Explore applications in measure theory and functional analysis\n✓ Solve problems involving sequences, series, and integrals\n✓ Study advanced topics like Lebesgue integration for deeper insights",
        inline=False
    )

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="theory", description="Learn about theories of math!")
async def learn_theory(interaction: discord.Interaction, topic: str):
    topics = {
        "set theory": {
            "description": "The study of sets and their properties, forming the foundation of modern mathematics.",
            "content": "**Key Concepts:**\n• Sets and elements: A = {1, 2, 3}\n• Union: A ∪ B contains all elements in A or B\n• Intersection: A ∩ B contains elements in both A and B\n• Complement: A' contains elements not in A\n• Power set: P(A) = all subsets of A\n\n**Examples:**\n• If A = {1,2,3} and B = {2,3,4}: A ∪ B = {1,2,3,4}, A ∩ B = {2,3}\n• Venn diagrams visualize set relationships\n• Cardinal numbers: |{a,b,c}| = 3"
        },
        "graph theory": {
            "description": "Study of graphs (networks) with vertices and edges.",
            "content": "**Key Concepts:**\n• Vertices and edges\n• Directed and undirected graphs\n• Paths and cycles\n• Connectivity and components\n• Graph coloring and planar graphs\n\n**Examples:**\n• Complete graph K₄ has 4 vertices, each connected to 3 others\n• Shortest path problem: Find minimum distance between nodes\n• Degree of vertex: Number of edges connected to it\n• Eulerian path: Visit every edge exactly once"
        },
        "category theory": {
            "description": "Abstract study of mathematical structures and their relationships.",
            "content": "**Key Concepts:**\n• Objects and morphisms\n• Functors and natural transformations\n• Universal properties\n• Adjoint functors\n• Limits and colimits\n\n**Examples:**\n• Groups and group homomorphisms form a category\n• Functors map between categories\n• Natural transformation: Family of morphisms between functors\n• Universal property: Initial and terminal objects"
        },
        "chaos theory": {
            "description": "Study of dynamical systems exhibiting sensitive dependence on initial conditions.",
            "content": "**Key Concepts:**\n• Deterministic chaos\n• Butterfly effect: Small changes → large differences\n• Fractals and self-similarity\n• Lyapunov exponents\n• Attractors and bifurcations\n\n**Examples:**\n• Mandelbrot set: z → z² + c\n• Lorenz attractor: Models atmospheric convection\n• Logistic map: xₙ₊₁ = rxₙ(1-xₙ) exhibits chaos for r > 3.57\n• Double pendulum: Small initial differences lead to vastly different paths"
        },
        "information theory": {
            "description": "Mathematical study of information, communication, and entropy.",
            "content": "**Key Concepts:**\n• Entropy: H(X) = -Σ p(x)log₂(p(x))\n• Mutual information\n• Channel capacity\n• Huffman coding\n• Error correction codes\n\n**Examples:**\n• Fair coin flip: H = 1 bit\n• Shannon's source coding: Compress information optimally\n• Channel capacity: Maximum data transmission rate\n• Hamming code: Detects and corrects single-bit errors"
        }
    }
    
    topic = topic.lower()
    if topic in topics:
        topic_data = topics[topic]
        embed = discord.Embed(
            title=f"{topic.capitalize()} - Mathematical Theory",
            description=topic_data["description"],
            color=discord.Color.blurple()
        )
        embed.add_field(
            name="Theory & Examples",
            value=topic_data["content"],
            inline=False
        )
        embed.set_footer(text=f"Requested by {interaction.user.name} | Use /expert to practice")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title="Available Theories",
            description="set theory, graph theory, category theory, chaos theory, information theory",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Use /theory <topic> | Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="chaos", description="Learn about chaos theory")
async def chaos(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Chaos Theory",
        description="Study of dynamical systems exhibiting sensitive dependence on initial conditions.",
        color=discord.Color.orange()
    )
    embed.add_field(
        name="Key Concepts",
        value="• Deterministic chaos\n• Butterfly effect: Small changes → large differences\n• Fractals and self-similarity\n• Lyapunov exponents\n• Attractors and bifurcations",
        inline=False
    )
    embed.add_field(
        name="Examples",
        value="• Mandelbrot set: z → z² + c\n• Lorenz attractor: Models atmospheric convection\n• Logistic map: xₙ₊₁ = rxₙ(1-xₙ) exhibits chaos for r > 3.57\n• Double pendulum: Small initial differences lead to vastly different paths",
        inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="information", description="Learn about information theory")
async def information(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Information Theory",
        description="Mathematical study of information, communication, and entropy.",
        color=discord.Color.green()
    )
    embed.add_field(
        name="Key Concepts",
        value="• Entropy: H(X) = -Σ p(x)log₂(p(x))\n• Mutual information\n• Channel capacity\n• Huffman coding\n• Error correction codes",
        inline=False
    )
    embed.add_field(
        name="Examples",
        value="• Fair coin flip: H = 1 bit\n• Shannon's source coding: Compress information optimally\n• Channel capacity: Maximum data transmission rate\n• Hamming code: Detects and corrects single-bit errors",
        inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="category", description="Learn about category theory")
async def category(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Category Theory",
        description="Abstract study of mathematical structures and their relationships.",
        color=discord.Color.purple()
    )
    embed.add_field(
        name="Key Concepts",
        value="• Objects and morphisms\n• Functors and natural transformations\n• Universal properties\n• Adjoint functors\n• Limits and colimits",
        inline=False
    )
    embed.add_field(
        name="Examples",
        value="• Groups and group homomorphisms form a category\n• Functors map between categories\n• Natural transformation: Family of morphisms between functors\n• Universal property: Initial and terminal objects",
        inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="set", description="Learn about set theory")
async def set_theory(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Set Theory",
        description="The study of sets and their properties, forming the foundation of modern mathematics.",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Key Concepts",
        value="• Sets and elements: A = {1, 2, 3}\n• Union: A ∪ B contains all elements in A or B\n• Intersection: A ∩ B contains elements in both A and B\n• Complement: A' contains elements not in A\n• Power set: P(A) = all subsets of A",
        inline=False
    )
    embed.add_field(
        name="Examples",
        value="• If A = {1,2,3} and B = {2,3,4}: A ∪ B = {1,2,3,4}, A ∩ B = {2,3}\n• Venn diagrams visualize set relationships\n• Cardinal numbers: |{a,b,c}| = 3",
        inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="graph", description="Learn about graph theory")
async def graph_theory(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Graph Theory",
        description="Study of graphs (networks) with vertices and edges.",
        color=discord.Color.dark_orange()
    )
    embed.add_field(
        name="Key Concepts",
        value="• Vertices and edges\n• Directed and undirected graphs\n• Paths and cycles\n• Connectivity and components\n• Graph coloring and planar graphs",
        inline=False
    )
    embed.add_field(
        name="Examples",
        value="• Complete graph K₄ has 4 vertices, each connected to 3 others\n• Shortest path problem: Find minimum distance between nodes\n• Degree of vertex: Number of edges connected to it\n• Eulerian path: Visit every edge exactly once",
        inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.tree.command(name="sites", description="Get links to the best math learning resources online!")
async def sites(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Math Learning Resources",
        description="Here are some excellent online resources for learning mathematics:",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Khan Academy",
        value="[https://www.khanacademy.org/math](https://www.khanacademy.org/math)",
        inline=False
    )
    embed.add_field(
        name="MIT OpenCourseWare",
        value="[https://ocw.mit.edu](https://ocw.mit.edu)",
        inline=False
    )
    embed.add_field(
        name="Paul's Online Math Notes",
        value="[https://tutorial.math.lamar.edu](https://tutorial.math.lamar.edu)",
        inline=False
    )
    embed.set_footer(text=f"The Bests of Math! Requested by {interaction.user.name}")
    await interaction.response.send_message(embed=embed)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bot Info 
@bot.tree.command(name="info", description="Get information about the bot")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Math Learning Bot - Information",
        description="This bot is designed to help users learn various mathematical topics through interactive commands and resources.",
        color=discord.Color.gold()
    )
    embed.add_field(
        name="Developer",
        value="Developed by [Zig](@ziguratchy) on Discord",
        inline=False
    )
    embed.add_field(
        name="Purpose",
        value="To provide educational content and resources for learning mathematics in an engaging way.",
        inline=False
    )
    embed.add_field(
        name="Commands",
        value="/geometry, /calculus, /trigonometry, /statistics, /number, /combinatorics, /abstractalgebra, /realanalysis, /theory, /chaos, /information, /category, /set, /graph, /sites, /ais",
        inline=False
    )

bot.run("PUT YOUR SECRET TOKEN HERE")
