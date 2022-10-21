import Head from 'next/head';
import { Container, Heading, Text, Stack } from '@chakra-ui/react';

export default function Home() {
  const name = 'Lying Back Twist';
  const description =
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque consequat nisl lacinia orci mattis ullamcorper. Aenean at orci congue, imperdiet erat sed, pretium augue';
  const videoLink = 'https://www.youtube.com/watch?v=s9PzYuVwCSE';

  return (
    <div>
      <Head>
        <title>exercise</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Container py={16} maxW="3xl">
        <Stack spacing={4}>
          <Heading>{name}</Heading>

          <Text>{description}</Text>

          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/s9PzYuVwCSE"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          />
        </Stack>

        {/* <List>
          {exercises.map(e => (
            <Box bg="blue.500" w="100%" color="white" p={4} my={4} borderRadius={10} key={e}>
              {e}
            </Box>
          ))}
        </List> */}
      </Container>
    </div>
  );
}
