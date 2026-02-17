from  FireApp.models import Post, Category
from django.core.management.base import BaseCommand
from typing import Any
import random


    
class Command(BaseCommand):
    help="This command inserts post data"
    
    def handle(self, *args: Any, **options: Any):
        Post.objects.all().delete()
        
        titles=[
            "The Future of AI",
            "Climate Change Solutions",
            "Remote Work Trends",
            "Quantum Computing Explained",
            "Renewable Energy Innovations",
            "Deep Learning Demystified",
            "Post-Pandemic Economic Outlook",
            "Blockchain in Finance",
            "Storytelling in Marketing",
            "Medical Technology Advances",
            "Space Exploration Challenges",
            "Psychology of Decision Making",
            "Evolution of Social Media",
            "The Art of Cooking",
            "Cultural Diversity in Society",
            "Sustainable Development Investments",
            "Globalization Impact",
            "Power of Mindfulness",
            "Online Learning Revolution",
            "Art and Technology Fusion",    
]

        contents = [
    "Exploring the future of artificial intelligence and its impact on society. AI is poised to revolutionize various industries, from healthcare to finance, with its ability to analyze vast amounts of data and make predictions. As AI continues to evolve, ethical considerations and responsible usage will play a critical role in shaping its future.",

    "Discovering solutions to combat climate change and protect the environment. Through innovative technologies and sustainable practices, we can mitigate the effects of global warming and preserve our planet for future generations. Collective action by governments, businesses, and individuals is essential for long-term environmental sustainability.",

    "Analyzing trends and challenges in remote work environments. The shift to remote work has reshaped the way we work and collaborate, presenting both opportunities and challenges for organizations and employees. Effective communication tools and work-life balance are key to maintaining productivity in remote settings.",

    "An introduction to the principles and applications of quantum computing. Quantum computing holds the promise of solving complex problems that are intractable for classical computers, ushering in a new era of computation. This technology could significantly impact fields such as cryptography, medicine, and materials science.",

    "Investigating the latest innovations in renewable energy sources. From solar and wind power to biofuels and hydrogen, renewable energy technologies offer sustainable alternatives to fossil fuels and reduce greenhouse gas emissions. Continued investment in clean energy is vital for achieving global climate goals.",

    "Understanding the fundamentals of deep learning and neural networks. Deep learning algorithms mimic the human brain's neural networks to analyze complex data and make intelligent decisions, driving advancements in artificial intelligence. These models are widely used in image recognition, speech processing, and autonomous systems.",

    "Examining the economic landscape in the aftermath of the COVID-19 pandemic. The pandemic has reshaped global economies, accelerating digital transformation and highlighting the importance of resilience and adaptability. Governments and businesses are rethinking strategies to ensure sustainable economic recovery.",

    "Exploring the potential of blockchain technology in the financial sector. Blockchain technology has the potential to revolutionize financial transactions, offering transparency, security, and efficiency in peer-to-peer transactions. Its decentralized nature reduces reliance on intermediaries and enhances trust.",

    "Harnessing the power of storytelling to create compelling marketing campaigns. Storytelling is a powerful tool for brands to connect with their audience emotionally and convey their values and messages effectively. Strong narratives help build brand loyalty and customer engagement.",

    "Highlighting breakthroughs and advancements in medical technology. From precision medicine to telemedicine, medical technology innovations are transforming healthcare delivery and improving patient outcomes worldwide. These advancements increase access to care and enhance diagnostic accuracy.",

    "Addressing the obstacles and opportunities in space exploration. With renewed interest in space exploration, we are on the brink of new discoveries and advancements that will expand our understanding of the universe. International collaboration and private investment are accelerating progress in this field.",

    "Exploring the psychological factors influencing decision-making processes. Understanding human behavior and cognitive biases can help individuals and organizations make better decisions and achieve their goals. This knowledge is especially valuable in leadership, marketing, and policy-making.",

    "Tracing the evolution of social media platforms and their impact on society. Social media has reshaped how we communicate, connect, and consume information, influencing everything from politics to culture. It also raises important concerns about privacy, mental health, and misinformation.",

    "Celebrating the art of cooking and culinary creativity. Cooking is not just about nourishment but also about creativity, culture, and community, bringing people together through shared meals and experiences. Culinary traditions reflect history, identity, and personal expression.",

    "Promoting inclusivity and embracing diversity in modern communities. Embracing diversity fosters innovation, creativity, and mutual respect, creating vibrant and inclusive communities where everyone feels valued and empowered. Inclusive environments strengthen social cohesion and equality.",

    "Investigating sustainable development initiatives and their impact on the future. Sustainable development seeks to meet the needs of the present without compromising the ability of future generations to meet their own needs. It ensures a balance between economic growth, environmental protection, and social equity.",
    
    "Exploring the potential of blockchain technology in the financial sector. Blockchain technology has the potential to revolutionize financial transactions, offering transparency, security, and efficiency in peer-to-peer transactions. Its decentralized nature reduces reliance on intermediaries and enhances trust.",

    "Harnessing the power of storytelling to create compelling marketing campaigns. Storytelling is a powerful tool for brands to connect with their audience emotionally and convey their values and messages effectively. Strong narratives help build brand loyalty and customer engagement.",

    "Highlighting breakthroughs and advancements in medical technology. From precision medicine to telemedicine, medical technology innovations are transforming healthcare delivery and improving patient outcomes worldwide. These advancements increase access to care and enhance diagnostic accuracy.",

    "Addressing the obstacles and opportunities in space exploration. With renewed interest in space exploration, we are on the brink of new discoveries and advancements that will expand our understanding of the universe. International collaboration and private investment are accelerating progress in this field.",
    
        ]
          
        img_urls=[
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
]
        
        categories= Category.objects.all()
        for title, content, img_url in zip(titles ,contents, img_urls):
            category= random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        
        
       
    