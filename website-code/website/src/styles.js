import styled from 'styled-components';

export const Hero = styled.div`
    min-height: 100vh;
    width: 100%;
    background-color: black;
    /* background-image: url(https://i.pinimg.com/originals/99/8e/05/998e055aba57c24138220937cc5166ab.gif); */
    /* background-image: url(https://i.pinimg.com/originals/01/c9/41/01c941e746dfef3627e2d92a36198bd0.gif); */
    /* background-image: url(https://giffiles.alphacoders.com/211/211748.gif); */
    /* background-image: url(https://i.pinimg.com/originals/a3/c3/77/a3c3776b73f2ac4aa70ba7db2a5f66f6.gif); */
    background-image: url(https://i.imgur.com/KEnwbfZ.gif);

    background-position: center;
    background-repeat: no-repeat;
    background-size: 100%;
    color: white;
`;

export const Overlay = styled.div`
    opacity: 85%;
    width: 100%;
    height: 100%;
    z-index: 10;
    top: 0;
    left: 0;
    position: fixed;
`;

export const Video = styled.video`
    min-height: 100vh;
    width: 100%;
`;